# Bengaluru House Price Prediction

## Overview
This project aims to predict house prices in Bengaluru based on various features such as location, total square footage, number of bedrooms, and other factors. The model is trained on the `Bengaluru_House_Data.csv` dataset and deployed using Flask.

## Dataset
The dataset used for this project is `Bengaluru_House_Data.csv`, which contains information about various houses in Bengaluru, including:
- Location
- Total square feet
- Number of bedrooms (BHK)
- Number of bathrooms
- Price (target variable) and many more which were dropped during data cleaning.

## Technologies Used
- **Python** (for model development)
- **Jupyter Notebook** (for data preprocessing and model training)
- **Pandas, NumPy, Matplotlib, Seaborn** (for data analysis and visualization)
- **Scikit-Learn** (for model training and evaluation)
- **Flask** (for deploying the model as a web application)
- **HTML/CSS** (for frontend UI)

## Model Training
1. Data Cleaning: Handling missing values, outlier removal, and feature engineering.
2. Feature Selection: Identifying the most relevant features for predicting house prices.
3. Model Selection: Training different machine learning models and selecting the best one based on performance.
4. Saving the Model: The trained model is saved as a `pickle` file for deployment.

## Deployment
The trained model is deployed using Flask with the following structure:

- `index.html`: Landing page of the web application.
- `predict.html`: Form where users can input house details to get price predictions.
- `app.py`: Flask backend to handle requests and return predictions.
- `model.pkl`: Trained machine learning model.
- `columns.json`: JSON file containing column names used in the model.


