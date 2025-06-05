import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load labeled data
df = pd.read_csv('data/labeled_sensor_data.csv')

# Features and Target
X = df[['battery_voltage', 'motor_temperature', 'brake_pressure', 'tire_pressure']]
y = df['status']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model - Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("📊 Classification Report:")
print(classification_report(y_test, y_pred))

# Save Model
joblib.dump(model, 'models/battery_health_model.pkl')
print("✅ Model saved at models/battery_health_model.pkl")
