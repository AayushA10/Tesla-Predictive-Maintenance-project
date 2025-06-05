import streamlit as st
import requests
import random
import time
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="🚗 Tesla Live Monitoring", page_icon="🚗")

st.title("🚗 Tesla Predictive Maintenance - Live Monitoring")

# Initialize empty DataFrame to store live data
live_data = pd.DataFrame(columns=["timestamp", "battery_voltage", "motor_temperature", "brake_pressure", "tire_pressure", "status"])

# File path
csv_file_path = 'data/live_sensor_log.csv'

# If file doesn't exist, create it with headers
if not os.path.exists(csv_file_path):
    live_data.to_csv(csv_file_path, index=False)

placeholder = st.empty()

while True:
    # Random sensor values
    battery_voltage = random.uniform(370, 420)
    motor_temperature = random.uniform(60, 110)
    brake_pressure = random.uniform(30, 60)
    tire_pressure = random.uniform(30, 36)

    payload = {
        "battery_voltage": battery_voltage,
        "motor_temperature": motor_temperature,
        "brake_pressure": brake_pressure,
        "tire_pressure": tire_pressure
    }
    
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    result = response.json()

    # Add new row to DataFrame
    new_row = {
        "timestamp": pd.Timestamp.now(),
        "battery_voltage": battery_voltage,
        "motor_temperature": motor_temperature,
        "brake_pressure": brake_pressure,
        "tire_pressure": tire_pressure,
        "status": result["status"]
    }
    live_data = pd.concat([live_data, pd.DataFrame([new_row])], ignore_index=True)

    # Save new_row to CSV (append mode)
    new_row_df = pd.DataFrame([new_row])
    new_row_df.to_csv(csv_file_path, mode='a', header=False, index=False)

    with placeholder.container():
        st.subheader("🔋 Live Sensor Readings")
        st.metric("Battery Voltage (V)", f"{battery_voltage:.2f}")
        st.metric("Motor Temperature (°C)", f"{motor_temperature:.2f}")
        st.metric("Brake Pressure (psi)", f"{brake_pressure:.2f}")
        st.metric("Tire Pressure (psi)", f"{tire_pressure:.2f}")
        st.subheader(f"🚦 Vehicle Status: {'✅ OK' if result['status'] == 'OK' else '🚨 FAIL'}")
        
        # Plotting real-time graphs
        fig1 = px.line(live_data, x="timestamp", y="battery_voltage", title="Battery Voltage Over Time")
        st.plotly_chart(fig1, use_container_width=True)

        fig2 = px.line(live_data, x="timestamp", y="motor_temperature", title="Motor Temperature Over Time")
        st.plotly_chart(fig2, use_container_width=True)

    time.sleep(2)
