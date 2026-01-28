import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load('model.pkl')

# Custom title with heart
st.set_page_config(page_title="❤️ Heart Disease Prediction", page_icon="❤️")

# Beautiful header
st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1>❤️ Heart Disease Prediction App ❤️</h1>
        <p style='font-size: 18px; color: #FF6B6B;'>
            🫀 Predict Your Heart Health with AI 🫀
        </p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# Input features
st.header('💓 Enter Patient Information')

col1, col2 = st.columns(2)

with col1:
    age = st.slider('👤 Age', 20, 100, 50)
    sex = st.selectbox('⚧ Sex', [0, 1], format_func=lambda x: '👩 Female' if x == 0 else '👨 Male')
    cp = st.selectbox('🤕 Chest Pain Type', [0, 1, 2, 3], format_func=lambda x: ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'][x])
    trestbps = st.slider('🩸 Resting Blood Pressure (mm Hg)', 90, 200, 120)
    chol = st.slider('🧬 Serum Cholesterol (mg/dl)', 100, 600, 200)
    fbs = st.selectbox('🍬 Fasting Blood Sugar > 120 mg/dl', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')

with col2:
    restecg = st.selectbox('📊 Resting Electrocardiographic Results', [0, 1, 2])
    thalach = st.slider('⚡ Maximum Heart Rate Achieved', 70, 220, 150)
    exang = st.selectbox('🏃 Exercise Induced Angina', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    oldpeak = st.slider('📉 ST Depression Induced by Exercise', 0.0, 6.0, 1.0)
    slope = st.selectbox('📈 Slope of Peak Exercise ST Segment', [0, 1, 2])
    ca = st.slider('🚊 Number of Major Vessels', 0, 3, 0)

thal = st.selectbox('🩺 Thalassemia', [1, 2, 3, 6, 7], format_func=lambda x: {1: 'Normal', 2: 'Fixed Defect', 3: 'Reversible Defect', 6: 'Normal', 7: 'Reversible Defect'}[x])

st.divider()

# Predict button
if st.button('🔍 Predict Heart Health', use_container_width=True):
    features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]
    
    # Results container
    if prediction == 1:
        st.error(f"""
            ⚠️ **HIGH RISK** ⚠️
            
            Probability of heart disease: **{prob:.1%}**
            
            💔 Please consult with a healthcare professional immediately.
        """)
    else:
        st.success(f"""
            ✅ **LOW RISK** ✅
            
            Probability of heart disease: **{prob:.1%}**
            
            ❤️ Keep maintaining a healthy lifestyle!
        """)

st.divider()

# Footer
st.markdown("""
    <div style='text-align: center; padding: 20px; color: #666;'>
        <p>💊 <strong>Disclaimer:</strong> This app is for educational purposes only. 
        Always consult with qualified healthcare professionals for medical advice. ❤️</p>
    </div>
""", unsafe_allow_html=True)