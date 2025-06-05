import pandas as pd
import numpy as np

# Load the sensor data
df = pd.read_csv('data/sensor_data.csv')

# Create a new label column based on conditions:
# Fail (1) if battery voltage < 390V OR motor_temperature > 90°C
df['status'] = np.where((df['battery_voltage'] < 390) | (df['motor_temperature'] > 90), 1, 0)

# Save the new labeled dataset
df.to_csv('data/labeled_sensor_data.csv', index=False)

print("✅ Labeled data saved to data/labeled_sensor_data.csv")
