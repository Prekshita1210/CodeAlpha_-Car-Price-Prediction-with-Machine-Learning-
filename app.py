# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open("car_price_model.pkl", "rb") as file:
    model = pickle.load(file)


# Title
st.markdown("<h1 style='text-align: center; color: tomato;'></h1>", unsafe_allow_html=True)
st.markdown("""
<style>
.stApp{
background-color:Pink;"""
,unsafe_allow_html=True)


st.title("🚗 Car Price Prediction App")

# Input fields
present_price = st.number_input("Present Price (in Lakhs ₹)", min_value=0.0, step=0.1)
driven_kms = st.number_input("Kilometers Driven", min_value=0)
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
selling_type = st.selectbox("Selling Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
car_age = st.slider("Car Age (Years)", 0, 30, 5)

# Mapping for encoded inputs
fuel_map = {"Diesel": 0, "CNG": 1, "Petrol": 2}
selling_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Automatic": 0, "Manual": 1}

if st.button("Predict Selling Price"):
    input_data = np.array([
        present_price,
        driven_kms,
        fuel_map[fuel_type],
        selling_map[selling_type],
        trans_map[transmission],
        owner,
        car_age
    ]).reshape(1, -1)

    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Selling Price: ₹ {prediction:.2f} Lakhs")
