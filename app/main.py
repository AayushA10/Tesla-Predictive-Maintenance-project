from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize app
app = FastAPI()

# Load trained model
model = joblib.load('models/battery_health_model.pkl')

# Define input schema
class SensorData(BaseModel):
    battery_voltage: float
    motor_temperature: float
    brake_pressure: float
    tire_pressure: float

# Home route
@app.get("/")
def read_root():
    return {"msg": "🚗 Predictive Maintenance API is live!"}

# Prediction route
@app.post("/predict")
def predict(data: SensorData):
    # Convert input to dataframe
    input_df = pd.DataFrame([data.dict()])
    
    # Predict
    prediction = model.predict(input_df)[0]
    
    return {
        "prediction": int(prediction), 
        "status": "FAIL" if prediction == 1 else "OK"
    }
