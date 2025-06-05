import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data/sensor_data.csv')

# Basic Info
print("🔍 Data Head:")
print(df.head())

print("\n📊 Data Description:")
print(df.describe())

# Timestamp ko datetime bna le
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Battery Voltage Trend
plt.figure(figsize=(15, 6))
plt.plot(df['timestamp'], df['battery_voltage'], label='Battery Voltage (V)', color='blue')
plt.xlabel('Timestamp')
plt.ylabel('Voltage (V)')
plt.title('Battery Voltage Over Time')
plt.legend()
plt.tight_layout()
plt.savefig('data/battery_voltage_trend.png')  # 👈 SAVE graph here
plt.close()  # ⚡ Close kar de after saving

# Motor Temperature Distribution
plt.figure(figsize=(15, 6))
sns.histplot(df['motor_temperature'], kde=True, color='red')
plt.title('Motor Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.tight_layout()
plt.savefig('data/motor_temperature_distribution.png')  # 👈 SAVE graph here
plt.close()
