


📱 Mobile Price Range classification  (FastAPI)
🚀 Project Overview

This project builds a Machine Learning model to predict the price range category of a mobile phone based on its specifications such as RAM, Battery Power, Internal Memory, and more. the price range of a mobile phone based on its specifications.
The model is trained using scikit-learn and deployed on Hugging Face Spaces using Gradio.

The trained model is deployed using FastAPI, allowing real-time predictions through a REST API.

🎯 Problem Statement

Bob wants to compete with major mobile brands but does not know how to estimate phone pricing.

Instead of predicting exact prices, we classify phones into 4 price categories:

Price Range	Category
0	Low Cost
1	Medium Cost
2	High Cost
3	Very High Cost

This is a Multi-Class Classification Problem.

🧠 Machine Learning Model

Algorithm Used: Random Forest / SVM / Gradient Boosting

Train-Test Split: 80-20

Accuracy Achieved: ~90–95%

Important Features:

RAM

Battery Power

Internal Memory

Screen Resolution

🛠️ Tech Stack

Python

Scikit-learn

Pandas

FastAPI

Uvicorn

Joblib




## 🚀 Live Demo

You can enter mobile specifications and instantly get the predicted price category:

- 0 → Low Cost
- 1 → Medium Cost
- 2 → High Cost
- 3 → Very High Cost

---

## 🧠 Features Used in Model

The model uses the following input features:

- Battery Power
- Bluetooth (Yes/No)
- Clock Speed
- Dual SIM
- Front Camera
- 4G
- Internal Memory
- Mobile Depth
- Mobile Weight
- Number of Cores
- Primary Camera
- Pixel Height
- Pixel Width
- RAM
- Screen Height
- Screen Width
- Talk Time
- 3G
- Touch Screen
- WiFi

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Gradio
- Cloudpickle
- Hugging Face Spaces

---

📂 Project Structure
mobile-price-api/
│
├── app.py
├── mobile_price_model.pkl
├── train.csv
├── requirements.txt
└── README.md



deployment link :
https://jagruti512-mobile.hf.space/?logs=container&__theme=system&deep_link=j9Qt9_uCbqE














to get code & data kaggle link :https://www.kaggle.com/code/jagrutiyuvrajdhangar/mobile-price-range-classfication
