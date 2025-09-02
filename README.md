# Heart Disease Prediction Web App

## Overview
This project is a machine learning-based web application that predicts the risk of heart disease in patients using various health parameters. The model is trained on a dataset of patient records and can classify whether a patient is likely to have heart disease.

---

## Features
- Predicts the likelihood of heart disease based on patient data
- User-friendly web interface built with PyWebIO
- Uses Logistic Regression as the prediction model
- Displays results in an easy-to-understand format
- Supports input for multiple health parameters like age, sex, chest pain type, blood pressure, cholesterol, etc.

---

## Tech Stack
- **Programming Language:** Python 3.9
- **Web Framework:** Flask and PyWebIO
- **Machine Learning:** Scikit-learn (Logistic Regression)
- **Data Handling:** Pandas
- **Environment Management:** Virtual Environment (`venv`)

---

## Dataset
- The dataset used is `heart.csv`
- Features include:
  - Age
  - Sex
  - Chest pain type
  - Resting blood pressure
  - Cholesterol
  - Fasting blood sugar
  - Resting ECG results
  - Maximum heart rate achieved
  - Exercise induced angina
  - ST depression induced by exercise
  - Slope of ST segment
  - Number of major vessels colored by fluoroscopy
  - Thalassemia level
- Target column: `condition` (0 = No heart disease, 1 = Heart disease)

---

## How It Works
1. **Data Preprocessing**: Maps categorical inputs to numeric values for the model.
2. **Model Training**: Logistic Regression model is trained on the dataset and saved as `logmod.pkl`.
3. **Web Interface**: Users enter their health parameters through a form in the web app.
4. **Prediction**: Input is passed to the trained model, which predicts the risk of heart disease.
5. **Result Display**: The prediction is shown in a popup indicating high or low risk.

---

