import pytest
from app import app

@pytest.fixture
def client():
    # Configure Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Game Rating Prediction" in response.data

def test_prediction(client):
    """Test that the prediction endpoint works with valid data."""
    response = client.post('/predict', data={
        'platform_support': 3,
        'release_year': 2020,
        'release_month': 6,
        'price_original': 29.99,
        'price_final': 19.99,
        'user_reviews': 2000,
        'positive_ratio': 80
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'predicted_rating' in data
    assert 'similar_games' in data
