from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("mobile_price_model.pkl")

app = FastAPI(title="Mobile Price Range Prediction API")

# Input Schema
class MobileFeatures(BaseModel):
    battery_power: int
    blue: int
    clock_speed: float
    dual_sim: int
    fc: int
    four_g: int
    int_memory: int
    m_dep: float
    mobile_wt: int
    n_cores: int
    pc: int
    px_height: int
    px_width: int
    ram: int
    sc_h: int
    sc_w: int
    talk_time: int
    three_g: int
    touch_screen: int
    wifi: int

@app.get("/")
def home():
    return {"message": "Mobile Price Range Prediction API Running 🚀"}

@app.post("/predict")
def predict(data: MobileFeatures):
    features = np.array([[ 
        data.battery_power,
        data.blue,
        data.clock_speed,
        data.dual_sim,
        data.fc,
        data.four_g,
        data.int_memory,
        data.m_dep,
        data.mobile_wt,
        data.n_cores,
        data.pc,
        data.px_height,
        data.px_width,
        data.ram,
        data.sc_h,
        data.sc_w,
        data.talk_time,
        data.three_g,
        data.touch_screen,
        data.wifi
    ]])

    prediction = model.predict(features)

    return {"predicted_price_range": int(prediction[0])}
