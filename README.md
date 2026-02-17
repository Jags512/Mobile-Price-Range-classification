


📱 Mobile Price Range classification API (FastAPI)
🚀 Project Overview

This project builds a Machine Learning model to predict the price range category of a mobile phone based on its specifications such as RAM, Battery Power, Internal Memory, and more.

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

📂 Project Structure
mobile-price-api/
│
├── main.py
├── mobile_price_model.pkl
├── train.csv
├── requirements.txt
└── README.md

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/yourusername/mobile-price-api.git
cd mobile-price-api

2️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the API
uvicorn main:app --reload


Server will start at:

http://127.0.0.1:8000

📄 API Documentation (Swagger UI)

Open in browser:

http://127.0.0.1:8000/docs




🧾 requirements.txt
fastapi
uvicorn
scikit-learn
joblib
numpy
pandas
pydantic






to get code & data kaggle link :https://www.kaggle.com/code/jagrutiyuvrajdhangar/mobile-price-range-classfication
