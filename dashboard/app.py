import streamlit as st
import requests

st.set_page_config(page_title="🚗 Tesla Predictive Maintenance", page_icon="🚗")

st.title("🚗 Tesla Predictive Maintenance Dashboard")

# User Inputs
battery_voltage = st.number_input("Battery Voltage (V)", min_value=350.0, max_value=450.0, value=400.0)
motor_temperature = st.number_input("Motor Temperature (°C)", min_value=20.0, max_value=150.0, value=70.0)
brake_pressure = st.number_input("Brake Pressure (psi)", min_value=20.0, max_value=100.0, value=50.0)
tire_pressure = st.number_input("Tire Pressure (psi)", min_value=20.0, max_value=50.0, value=32.0)

if st.button("Predict Health Status"):
    payload = {
        "battery_voltage": battery_voltage,
        "motor_temperature": motor_temperature,
        "brake_pressure": brake_pressure,
        "tire_pressure": tire_pressure
    }
    
    # API Request
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    result = response.json()
    
    st.subheader("Prediction Result:")
    if result["status"] == "OK":
        st.success("✅ Vehicle Status: OK")
    else:
        st.error("🚨 Vehicle Status: FAIL")
