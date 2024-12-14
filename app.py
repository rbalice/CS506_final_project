from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np
import traceback
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load model and data
try:
    model = joblib.load('model.pkl')
    games_cleaned = pd.read_csv('games_cleaned.csv')
except Exception as e:
    logger.error(f"Error loading model or data: {e}")
    logger.error(traceback.format_exc())

def convert_platform_support(value):
    mapping = {
        7: 'Windows, Mac, Linux',
        6: 'Windows, Mac',
        5: 'Windows, Linux',
        4: 'Mac, Linux',
        3: 'Windows',
        2: 'Mac',
        1: 'Linux',
        0: 'No Platform'
    }
    return mapping.get(value, 'Unknown')

def find_similar_games(games_df, input_features, top_n=3):
    features_columns = [
        'platform_support', 
        'release_year', 
        'release_month', 
        'price_final', 
        'price_original',
        'positive_ratio',
        'user_reviews'
    ]
    
    games_df['distance'] = np.sqrt(
        ((games_df[features_columns] - input_features[features_columns].iloc[0]) ** 2).sum(axis=1)
    )
    
    similar_games = games_df.sort_values('distance').head(top_n)
    similar_games['platform_support'] = similar_games['platform_support'].map(convert_platform_support)
    return similar_games

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Log all incoming form data
        logger.debug("Received form data:")
        for key, value in request.form.items():
            logger.debug(f"{key}: {value}")

        # Extract and convert form data with explicit error handling
        try:
            platform_support = int(request.form['platform_support'])
            release_year = int(request.form['release_year'])
            release_month = int(request.form['release_month'])
            price_final = float(request.form['price_final'])
            price_original = float(request.form['price_original'])
            positive_ratio = float(request.form['positive_ratio'])
            user_reviews = int(request.form['user_reviews'])
        except ValueError as ve:
            logger.error(f"Value conversion error: {ve}")
            return jsonify({'error': f'Invalid input format: {str(ve)}'}), 400
        except KeyError as ke:
            logger.error(f"Missing form field: {ke}")
            return jsonify({'error': f'Missing form field: {str(ke)}'}), 400

        # Create input DataFrame
        input_data = pd.DataFrame({
            'positive_ratio': [positive_ratio],
            'user_reviews': [user_reviews],
            'platform_support': [platform_support],
            'release_year': [release_year],
            'release_month': [release_month],
            'price_final': [price_final],
            'price_original': [price_original]
        })

        # Log input data
        logger.debug(f"Input DataFrame:\n{input_data}")

        # Predict and find similar games
        try:
            predicted_rating = model.predict(input_data)[0]
            similar_games = find_similar_games(games_cleaned, input_data)
            similar_games_list = similar_games.to_dict('records')

            return jsonify({
                'predicted_rating': float(predicted_rating),
                'similar_games': similar_games_list
            })
        except Exception as pred_error:
            logger.error(f"Prediction error: {pred_error}")
            logger.error(traceback.format_exc())
            return jsonify({'error': 'Prediction failed'}), 500

    except Exception as e:
        logger.error(f"Unexpected error in predict route: {e}")
        logger.error(traceback.format_exc())
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)