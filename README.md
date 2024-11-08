# CS506_final_project

## Project Description
Studying the relationship between video game data and sales is of significant importance. Firstly, this research can help developers and publishers better understand player behavior and preferences, allowing them to optimize video game design and marketing strategies. Additionally, such research can provide valuable market insights for investors, helping them assess the potential success and risks associated with a video game. Finally, understanding the relationship between video game data and sales contributes to the healthy development of the entire industry, guiding future innovations. Therefore, a deep analysis of this data is crucial not only for the success of individual video games but also for the evolution and growth of the entire gaming ecosystem.

Update: Achieving the new goal can provide a way to recommend user about games they might be more interested in.

## Goal
The goal of this project is to predict sales of video games in different regions based on their genre, platform, publisher, and release year.

Update: Because the data set has changed and it doesn't include features like number of sales, so I planned to add a goal of predicting a user's rating to a game with providing features.

## Data Collection
We will need a dataset that collects video games with their genre, platform, publisher, release year, and sales in different regions. The dataset will be obtained from Kaggle: EDA - VIDEO GAME SALES (https://www.kaggle.com/code/upadorprofzs/eda-video-game-sales#EDA---VIDEO-GAME-SALES-%F0%9F%8E%AE). This dataset was generated by scraping vgchartz.com.

Update: A new data set collected game recommendations on steam, including three files:

games.csv - a table of games (or add-ons) information on ratings, pricing in US dollars $, release date, etc. A piece of extra non-tabular details on games, such as descriptions and tags, is in a metadata file;

users.csv - a table of user profiles' public information: the number of purchased products and reviews published;

recommendations.csv - a table of user reviews: whether the user recommends a product. The table represents a many-many relation between a game entity and a user entity.
The link of this data set is (https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam/data).

## Modeling Plan
We plan to use clustering, decision trees, regression, and time series analysis to model the dataset.

Update: Currently using linear regression to model the dataset.

## Visualize Plan
We plan to use scatter plots, decision tree visualizations, regression scatter plots, and time series plots to visualize our data.

Update: Currently we use bar plot to plot the relation between game rating and other features to show pattern.

## Test Plan
We use 70% of the data for training and 30% of the data for testing.

## Video
(https://youtu.be/oEmzQSd4EVs)
