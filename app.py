import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load('model.pkl')

# Title
st.title('Heart Disease Prediction App')

# Input features
st.header('Enter Patient Information')

age = st.slider('Age', 20, 100, 50)
sex = st.selectbox('Sex', [0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3], format_func=lambda x: ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'][x])
trestbps = st.slider('Resting Blood Pressure (mm Hg)', 90, 200, 120)
chol = st.slider('Serum Cholesterol (mg/dl)', 100, 600, 200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
thalach = st.slider('Maximum Heart Rate Achieved', 70, 220, 150)
exang = st.selectbox('Exercise Induced Angina', [0, 1])
oldpeak = st.slider('ST Depression Induced by Exercise', 0.0, 6.0, 1.0)
slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
ca = st.slider('Number of Major Vessels Colored by Flourosopy', 0, 3, 0)
thal = st.selectbox('Thalassemia', [1, 2, 3, 6, 7], format_func=lambda x: {1: 'Normal', 2: 'Fixed Defect', 3: 'Reversible Defect', 6: 'Normal', 7: 'Reversible Defect'}[x])

# Predict
if st.button('Predict'):
    features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]
    
    if prediction == 1:
        st.error(f'High risk of heart disease. Probability: {prob:.2f}')
    else:
        st.success(f'Low risk of heart disease. Probability: {prob:.2f}')