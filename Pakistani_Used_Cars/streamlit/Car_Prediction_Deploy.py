import pandas as pd
import streamlit as st
import pickle
import os

# Load car data

with open(https://github.com/abdullaharif381/Intro-to-Data-Science/blob/main/Pakistani_Used_Cars/streamlit/deploy_car_df.pickle, 'rb') as f:
    car_data = pickle.load(f)

car_data = pd.DataFrame(car_data)

# Load the model


with open(https://github.com/abdullaharif381/Intro-to-Data-Science/blob/main/Pakistani_Used_Cars/streamlit/deploy_car.pickle, 'rb') as f:
    model = pickle.load(f)

# Streamlit app
st.title("Used Car Worth Estimators")

# Rest of your code...

# Input fields
name = st.selectbox("Enter the car company", car_data["car_name"].unique())
year = st.selectbox("Enter the car manufacturing date", sorted(car_data["model_year"].unique()))
capacity = st.text_input("Enter the car capacity in CC", key="capacity_cc")

# Check if the input is not empty before converting to int
if capacity:
    try:
        capacity = int(capacity)
        st.write(f"Capacity entered: {capacity} CC")
    except ValueError:
        st.error("Please enter a valid integer for capacity.")
else:
    st.warning("Please enter a value for capacity.")

km = st.text_input("Enter the car distance driven", key="kilometers_input")

# Check if the input is not empty before converting to int
if km:
    try:
        km = int(km)
        st.write(f"Kilometers entered: {km}")
    except ValueError:
        st.error("Please enter a valid integer for kilometers.")
else:
    st.warning("Please enter a value for kilometers.")

trans = st.selectbox("Enter the transmission type of the car", sorted(car_data["transmission"].unique()))
fuel = st.selectbox("Enter the car fuel type", car_data["engine_type"].unique())
features = st.selectbox("Enter the number of features your car has", car_data["car_features_clean"].unique())
types = st.selectbox("Enter the body type of your car", car_data["body_type"].unique())
province = st.selectbox("Enter the province of the car", ["Islamabad", "Punjab", "Sindh", "Balochistan", "KPK"])

# Convert categorical features to numerical
transit = 1 if trans == 'Automatic' else 0
engines = 3 if fuel == 'Diesel' else (2 if fuel == 'Hybrid' else 1)

# Create a sample DataFrame
sample = pd.DataFrame([[name, province, year, km, transit, features, capacity, types, engines]],
                      columns=['car_name', "province", "model_year", 'mileage', 'transmission',
                               "car_features_clean", 'engine_capacity', 'body_type', 'engine_type'])

# Debugging Output
st.write("Debugging Output:")
st.write(sample)

# Attempt the prediction
try:
    predicted_price = model.predict(sample)
    predicted_inflated_price = predicted_price*1.28
    res = '{:,}'.format(round(int(predicted_inflated_price),-2))
   # st.write(f"Predicted Price: {res}")
except Exception as e:
    st.error(f"Error during prediction: {e}")


if st.button("Predict"):
    st.text("Rs.")
    st.title(res)
