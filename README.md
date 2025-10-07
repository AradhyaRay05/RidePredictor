# RidePredictor – Predicting Daily Bike Rental Demand

## Project Goal
RidePredictor aims to predict the daily demand for bike rentals based on various environmental and seasonal factors. This project provides insights into rental patterns, helping bike-sharing companies optimize their operations and improve customer satisfaction.

---

## Overview
This project leverages **machine learning models** to predict the number of bike rentals on a given day. The dataset includes features such as weather conditions, temperature, humidity, and time-related attributes. The model was trained, evaluated, and deployed as an interactive application for real-time predictions.

---

## Project Workflow

### 1. Data Preprocessing
- Handled missing values and ensured data consistency.
- Renamed columns for better readability and consistency.
- Extracted date-related features such as:
  - **Month**
  - **Day of the week**
  - **Weekend indicator**
- Encoded categorical variables using **One-Hot Encoding** for features like:
  - Seasons
  - Functioning Day
- Scaled numerical features using **MinMaxScaler** to normalize the data.
- Visualized data distributions and relationships to identify trends and outliers

### 2. Model Building
- Used **Random Forest Regressor** as the primary model for prediction.
- Trained the model on the processed dataset using default hyperparameters.
- Saved the trained model (`model.pkl`) and scaler (`scaler.pkl`) for deployment.

### 3. Evaluation Metrics
- Evaluated the model on test data using the following metrics:
  - **Mean Squared Error (MSE):**
    - Train: 1.5458
    - Test: 12.6041
  - **Root Mean Squared Error (RMSE):**
    - Train: 1.2433
    - Test: 3.5502
  - **Mean Absolute Error (MAE):**
    - Train: 0.7937
    - Test: 2.1947
  - **R² Score:**
    - Train: 0.9900
    - Test: 0.9202
- Visualized residuals and feature importance to validate model performance.

### 4. Deployment
- Developed a **Streamlit web app** (`app.py`) for user interaction.
- Integrated the trained model and preprocessing pipeline.
- Features of the deployed app:
  - User-friendly input interface with sliders and dropdowns.
  - Real-time predictions for daily bike rental demand.
  - Visualizations of input data and predictions.
  - Option to upload CSV files for batch predictions.

---



