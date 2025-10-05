import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler

try:
    with open('model.pkl', 'rb') as f:
        rf_model = pickle.load(f)
except FileNotFoundError:
    st.error("Error: Model file not found.")
    rf_model = None

try:
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
except FileNotFoundError:
    st.error("Error: Scaler file not found.")
    scaler = None

st.title("Seoul Bike Demand Prediction")
st.sidebar.header("Input Features")
def user_input_features():
    hour = st.sidebar.slider("Hour", 0, 23, 12)
    temperature = st.sidebar.slider("Temperature (°C)", -20.0, 40.0, 10.0)
    humidity = st.sidebar.slider("Humidity (%)", 0, 100, 50)
    wind_speed = st.sidebar.slider("Wind speed (m/s)", 0.0, 8.0, 2.0)
    visibility = st.sidebar.slider("Visibility (10m)", 0, 2000, 1000)
    solar_radiation = st.sidebar.slider("Solar Radiation (MJ/m2)", 0.0, 4.0, 1.0)
    rainfall = st.sidebar.slider("Rainfall (mm)", 0.0, 40.0, 0.0)
    snowfall = st.sidebar.slider("Snowfall (cm)", 0.0, 10.0, 0.0)
    seasons = st.sidebar.selectbox("Seasons", ('Autumn', 'Spring', 'Summer', 'Winter'))
    holiday = st.sidebar.selectbox("Holiday", ('No Holiday', 'Holiday'))
    functioning_day = st.sidebar.selectbox("Functioning Day", ('Yes', 'No'))
    month = st.sidebar.slider("Month", 1, 12, 6)
    weekdays_weekend = st.sidebar.selectbox("Weekday or Weekend", (0, 1), format_func=lambda x: 'Weekday' if x == 0 else 'Weekend')
    data = {
        'Hour': hour,
        'Temperature': temperature,
        'Humidity': humidity,
        'Wind_speed': wind_speed,
        'Visibility': visibility,
        'Solar_Radiation': solar_radiation,
        'Rainfall': rainfall,
        'Snowfall': snowfall,
        'Seasons': seasons,
        'Holiday': holiday,
        'Functioning_Day': functioning_day,
        'month': month,
        'weekdays_weekend': weekdays_weekend
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

categorical_cols = ['Hour', 'Seasons', 'Holiday', 'Functioning_Day', 'month', 'weekdays_weekend']
for col in categorical_cols:
    if col in input_df.columns:
        input_df[col] = input_df[col].astype('category')

input_df_encoded = input_df.copy()
for col in ['Hour', 'Seasons', 'Holiday', 'Functioning_Day', 'month', 'weekdays_weekend']:
    if col in input_df_encoded.columns:
        all_categories = None
        if col == 'Hour':
            all_categories = [str(i) for i in range(24)] 
        elif col == 'Seasons':
            all_categories = ['Autumn', 'Spring', 'Summer', 'Winter']
        elif col == 'Holiday':
            all_categories = ['Holiday', 'No Holiday']
        elif col == 'Functioning_Day':
             all_categories = ['No', 'Yes']
        elif col == 'month':
             all_categories = [str(i) for i in range(1, 13)] 
        elif col == 'weekdays_weekend':
             all_categories = [0, 1]


        if all_categories:
             input_df_encoded = pd.get_dummies(input_df_encoded, columns=[col], prefix=col)
             for cat in all_categories:
                 dummy_col_name = f"{col}_{cat}"
                 if dummy_col_name not in input_df_encoded.columns:
                     input_df_encoded[dummy_col_name] = False

input_df_encoded = input_df_encoded.drop(columns=categorical_cols, errors='ignore')
expected_columns_after_encoding = [
    'Temperature', 'Humidity', 'Wind_speed', 'Visibility', 'Solar_Radiation', 'Rainfall', 'Snowfall',
    'Hour_1', 'Hour_2', 'Hour_3', 'Hour_4', 'Hour_5', 'Hour_6', 'Hour_7', 'Hour_8', 'Hour_9',
    'Hour_10', 'Hour_11', 'Hour_12', 'Hour_13', 'Hour_14', 'Hour_15', 'Hour_16', 'Hour_17',
    'Hour_18', 'Hour_19', 'Hour_20', 'Hour_21', 'Hour_22', 'Hour_23',
    'Seasons_Spring', 'Seasons_Summer', 'Seasons_Winter',
    'Holiday_No Holiday',
    'Functioning_Day_Yes',
    'month_2', 'month_3', 'month_4', 'month_5', 'month_6', 'month_7', 'month_8', 'month_9',
    'month_10', 'month_11', 'month_12',
    'weekdays_weekend_1'
]

input_df_aligned = input_df_encoded.reindex(columns=expected_columns_after_encoding, fill_value=0)

for col in input_df_aligned.columns:
    if input_df_aligned[col].dtype == 'bool':
        input_df_aligned[col] = input_df_aligned[col].astype(int)
numerical_cols_aligned = [col for col in expected_columns_after_encoding if col in ['Temperature', 'Humidity', 'Wind_speed', 'Visibility', 'Solar_Radiation', 'Rainfall', 'Snowfall']]
if scaler is not None:
    input_df_aligned[numerical_cols_aligned] = scaler.transform(input_df_aligned[numerical_cols_aligned])
else:
    st.warning("Scaler not loaded. Numerical features will not be scaled.")

st.subheader("User Input features")
st.write(input_df)
st.subheader("Processed Input features (for prediction)")
st.write(input_df_aligned)

if rf_model is not None:
    if st.button("Predict Rented Bike Count"):
        try:
            prediction_sqrt = rf_model.predict(input_df_aligned)
            predicted_bike_count = prediction_sqrt[0]**2
            st.subheader("Prediction")
            st.write(f"Predicted Rented Bike Count: {predicted_bike_count:.2f}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")