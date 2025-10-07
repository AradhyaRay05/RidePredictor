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
