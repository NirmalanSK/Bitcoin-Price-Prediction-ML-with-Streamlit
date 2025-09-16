# Bitcoin Price Prediction with Machine Learning and Streamlit

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)  
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)  
![scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-yellow)  

## 📌 Project Overview
This project demonstrates how to build and deploy a **Machine Learning model** to predict Bitcoin prices using **historical data**.  
It uses:
- **scikit-learn** for model training and evaluation  
- **Streamlit** for interactive web deployment  
- **pandas & numpy** for data processing  
- **matplotlib/seaborn** for visualization  

The app allows users to input/visualize data and view **predicted Bitcoin prices** in real-time.

---

## 🚀 Features
- Load and preprocess Bitcoin price dataset  
- Train ML models for regression tasks (Random Forest, Linear Regression, etc.)  
- Visualize actual vs. predicted Bitcoin prices  
- Interactive **Streamlit Web App**  

---

## 📂 Project Structure
├── app.py # Streamlit app script
├── BitCoin-Price-Prediction-ML-with-Streamlit.ipynb # Jupyter notebook (model training)
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── models/ # Saved ML models (pickle files)

---
## Dataset
The dataset contains historical Bitcoin price data.
- Preprocessing steps include:
- Handling missing values
- Feature scaling (MinMaxScaler)
- Splitting into training and testing sets
---
## Machine Learning
- Algorithms used:
- Random Forest Regressor
- Linear Regression / Ridge / Lasso
- Evaluation metrics:
   - Mean Absolute Error (MAE)
   - Mean Squared Error (MSE)
   - R² Score
---
## 🛠 Installation
### Install dependencies:

pip install -r requirements.txt
---
### Run the Streamlit app:
streamlit run app.py
---
### local web app at:
http://localhost:8501
---
### app can be deployed on Streamlit Cloud
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-link)

---


Clone the repository:
```bash
git clone https://github.com/NirmalanSK/Bitcoin-Price-Prediction-ML-with-Streamlit.git
cd Bitcoin-Price-Prediction-ML-with-Streamlit

---
