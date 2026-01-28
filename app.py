import streamlit as st
import joblib
import numpy as np
import time

# Load the model
model = joblib.load('model.pkl')

# Custom title with heart
st.set_page_config(
    page_title="❤️ Heart Disease Prediction", 
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
    <style>
        /* Main background */
        .stApp {
            background: linear-gradient(135deg, #0f0f3d 0%, #1a1a5c 50%, #2d0d4d 100%);
        }
        
        /* Header styling */
        .header-container {
            text-align: center;
            padding: 50px 20px;
            background: linear-gradient(135deg, #FF1744 0%, #FF6B6B 50%, #FF8E53 100%);
            border-radius: 20px;
            box-shadow: 0 15px 50px rgba(255, 23, 68, 0.4);
            margin-bottom: 40px;
            animation: pulse 3s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { box-shadow: 0 15px 50px rgba(255, 23, 68, 0.4); }
            50% { box-shadow: 0 15px 60px rgba(255, 23, 68, 0.6); }
        }
        
        .header-title {
            font-size: 3.5em;
            font-weight: 900;
            color: white;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
            margin: 0;
            letter-spacing: 2px;
        }
        
        .header-subtitle {
            font-size: 1.4em;
            color: white;
            margin-top: 15px;
            opacity: 0.98;
            font-weight: 600;
        }
        
        /* Input section styling */
        .input-section {
            background: rgba(255, 255, 255, 0.97);
            border-radius: 20px;
            padding: 40px;
            margin: 30px 0;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
            border: 2px solid rgba(255, 23, 68, 0.1);
        }
        
        /* Prediction result styling */
        .result-high-risk {
            background: linear-gradient(135deg, #FF1744 0%, #FF6B6B 100%);
            padding: 40px;
            border-radius: 20px;
            color: white;
            text-align: center;
            box-shadow: 0 15px 50px rgba(255, 23, 68, 0.4);
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .result-low-risk {
            background: linear-gradient(135deg, #00C853 0%, #69F0AE 100%);
            padding: 40px;
            border-radius: 20px;
            color: white;
            text-align: center;
            box-shadow: 0 15px 50px rgba(0, 200, 83, 0.4);
            border: 2px solid rgba(255, 255, 255, 0.2);
        }
        
        .result-title {
            font-size: 2.8em;
            font-weight: 900;
            margin: 10px 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        .result-probability {
            font-size: 2.2em;
            margin: 20px 0;
            font-weight: bold;
            letter-spacing: 1px;
        }
        
        .result-message {
            font-size: 1.15em;
            margin-top: 20px;
            line-height: 1.8;
            font-weight: 500;
        }
        
        /* Button styling */
        .stButton > button {
            width: 100%;
            padding: 18px;
            font-size: 1.1em;
            font-weight: bold;
            border-radius: 15px;
            background: linear-gradient(135deg, #FF1744 0%, #FF6B6B 100%);
            color: white;
            border: none;
            box-shadow: 0 6px 20px rgba(255, 23, 68, 0.3);
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(255, 23, 68, 0.5);
        }
        
        .stButton > button:active {
            transform: translateY(-1px);
        }
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 15px 25px;
            color: white;
            font-weight: 600;
            font-size: 1.05em;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #FF1744 0%, #FF6B6B 100%);
            color: white;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a1a3f 0%, #2d0d4d 100%);
        }
        
        /* Metric styling */
        .stMetric {
            background: rgba(255, 255, 255, 0.05);
            padding: 15px;
            border-radius: 12px;
            border: 1px solid rgba(255, 23, 68, 0.2);
        }
        
        /* Info/Warning/Success box styling */
        .stInfo, .stWarning, .stSuccess, .stError {
            border-radius: 12px;
            padding: 15px;
            font-weight: 500;
        }
        
        /* Expander styling */
        .streamlit-expanderHeader {
            font-size: 1.1em;
            font-weight: 600;
        }
        
        /* Divider styling */
        hr {
            border: 1px solid rgba(255, 23, 68, 0.2);
            margin: 25px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Beautiful header
st.markdown("""
    <div class='header-container'>
        <h1 class='header-title'>❤️ Heart Disease Prediction</h1>
        <p class='header-subtitle'>🫀 Elite AI-Powered Health Assessment 🫀</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar with model info
with st.sidebar:
    st.markdown("### 📊 Model Information")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🎯 Accuracy", "88.33%")
    with col2:
        st.metric("📈 Samples", "297")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🌳 Trees", "100")
    with col2:
        st.metric("📊 Features", "13")
    
    st.markdown("---")
    st.markdown("### ⚙️ System Status")
    st.success("✅ Production Ready")
    st.info("🤖 Random Forest Model")
    
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.warning("""
    ✅ Enter accurate medical data
    
    ⚠️ Screening tool only
    
    🏥 Consult professionals
    """)

# Welcome section
with st.expander("📖 About This App", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🏥 Overview
        
        Advanced heart disease prediction system using AI and machine learning.
        
        **Features:**
        - 🤖 AI-Powered Analysis
        - 📊 Real-time Predictions
        - 💡 Personalized Insights
        - 📈 Risk Visualization
        """)
    with col2:
        st.markdown("""
        ### 📈 Performance Metrics
        
        **Accuracy:** 88.33% ⭐
        
        **Precision:** High Confidence
        
        **Type:** Classification
        
        **Validation:** Cross-Tested
        """)

# Input features section
st.markdown("<div class='input-section'>", unsafe_allow_html=True)
st.markdown("## 💓 Enter Patient Information")
st.markdown("*Please provide accurate medical information for better predictions*")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Personal & Demographic Info")
    age = st.slider('👤 Age (years)', 20, 100, 50, help="Patient's age in years")
    sex = st.selectbox('⚧ Sex', [0, 1], format_func=lambda x: '👩 Female' if x == 0 else '👨 Male')
    
    st.markdown("### Blood & Metabolic Indicators")
    chol = st.slider('🧬 Serum Cholesterol (mg/dl)', 100, 600, 200, help="Total cholesterol level")
    fbs = st.selectbox('🍬 Fasting Blood Sugar > 120 mg/dl', [0, 1], format_func=lambda x: 'No ✅' if x == 0 else 'Yes ⚠️')
    trestbps = st.slider('🩸 Resting Blood Pressure (mm Hg)', 90, 200, 120, help="Systolic blood pressure")

with col2:
    st.markdown("### Cardiac Assessment")
    cp = st.selectbox('🤕 Chest Pain Type', [0, 1, 2, 3], format_func=lambda x: ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'][x])
    thalach = st.slider('⚡ Maximum Heart Rate Achieved', 70, 220, 150, help="Peak heart rate during exercise")
    exang = st.selectbox('🏃 Exercise Induced Angina', [0, 1], format_func=lambda x: 'No ✅' if x == 0 else 'Yes ⚠️')
    
    st.markdown("### ST Segment & Other Factors")
    oldpeak = st.slider('📉 ST Depression (Exercise)', 0.0, 6.0, 1.0, help="ST segment depression")
    slope = st.selectbox('📈 Slope of Peak ST Segment', [0, 1, 2], format_func=lambda x: ['Upsloping', 'Flat', 'Downsloping'][x])

st.markdown("### Additional Health Indicators")
col3, col4 = st.columns(2)
with col3:
    ca = st.slider('🚊 Major Vessels (Fluoroscopy)', 0, 3, 0, help="Number of major vessels colored")
with col4:
    thal = st.selectbox('🩺 Thalassemia', [1, 2, 3, 6, 7], format_func=lambda x: {1: 'Normal', 2: 'Fixed Defect', 3: 'Reversible Defect', 6: 'Normal', 7: 'Reversible Defect'}[x])
    restecg = st.selectbox('📊 Resting ECG Results', [0, 1, 2], format_func=lambda x: ['Normal', 'ST-T Abnormality', 'LVH'][x])

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")

# Prediction button
st.markdown("## 🔮 AI Prediction")
prediction_button = st.button('🔍 Analyze Heart Health', use_container_width=True)

if prediction_button:
    # Show loading animation
    with st.spinner('🤖 AI is analyzing your data...'):
        time.sleep(1)
        
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        prediction = model.predict(features)[0]
        prob = model.predict_proba(features)[0]
        
        prob_no_disease = prob[0]
        prob_disease = prob[1]
    
    # Display results
    st.markdown("### 📊 Prediction Results")
    
    if prediction == 1:
        # High Risk Result
        st.markdown(f"""
            <div class='result-high-risk'>
                <div class='result-title'>⚠️ HIGH RISK ALERT ⚠️</div>
                <div class='result-probability'>Heart Disease Risk: {prob_disease:.1%}</div>
                <div class='result-probability'>Safe Probability: {prob_no_disease:.1%}</div>
                <div class='result-message'>
                    💔 The AI model indicates a higher risk of heart disease.<br>
                    🏥 <strong>IMPORTANT:</strong> Seek medical attention immediately<br>
                    📋 Schedule an appointment with a cardiologist as soon as possible
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        # Low Risk Result
        st.markdown(f"""
            <div class='result-low-risk'>
                <div class='result-title'>✅ LOW RISK ✅</div>
                <div class='result-probability'>Heart Disease Risk: {prob_disease:.1%}</div>
                <div class='result-probability'>Safe Probability: {prob_no_disease:.1%}</div>
                <div class='result-message'>
                    ❤️ Good news! The AI indicates a lower risk of heart disease.<br>
                    💪 Keep maintaining a healthy lifestyle<br>
                    📍 Continue regular health check-ups and exercise
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Additional insights
    st.markdown("---")
    st.markdown("### 💡 Key Health Insights")
    
    col_insights1, col_insights2 = st.columns(2)
    
    with col_insights1:
        st.markdown(f"""
        **📈 Your Vitals Summary:**
        - 🫀 Heart Rate: {thalach} bpm
        - 🩸 Blood Pressure: {trestbps} mm Hg
        - 🧬 Cholesterol: {chol} mg/dl
        - 👤 Age: {age} years
        """)
    
    with col_insights2:
        st.markdown(f"""
        **🎯 Risk Factors Detected:**
        - Chest Pain Type: {"Present ⚠️" if cp > 0 else "None ✅"}
        - Exercise Angina: {"Yes ⚠️" if exang == 1 else "No ✅"}
        - High Cholesterol: {"Yes ⚠️" if chol > 240 else "No ✅"}
        - Elevated BP: {"Yes ⚠️" if trestbps > 140 else "No ✅"}
        """)
    
    # Recommendations
    st.markdown("---")
    st.markdown("### 📋 Personalized Recommendations")
    
    recommendations = []
    if chol > 240:
        recommendations.append("🥗 Reduce cholesterol intake - limit saturated fats and processed foods")
    if trestbps > 140:
        recommendations.append("🧂 Reduce sodium intake and manage stress levels")
    if thalach < 100:
        recommendations.append("🏃 Increase cardiovascular exercise - aim for 150 mins/week")
    if exang == 1:
        recommendations.append("⚕️ Consult your doctor before increasing exercise intensity")
    if age > 60:
        recommendations.append("📊 Schedule regular cardiac check-ups")
    
    if not recommendations:
        recommendations.append("✅ Maintain your current healthy lifestyle!")
        recommendations.append("💪 Continue regular exercise and balanced diet")
    
    for i, rec in enumerate(recommendations, 1):
        st.markdown(f"**{i}. {rec}**")

st.markdown("---")
st.markdown("""
    <div class='footer'>
        <p style='font-size: 0.9em; color: rgba(255,255,255,0.7);'>
            💊 For educational purposes. Always consult healthcare professionals. 🏥
        </p>
    </div>
""", unsafe_allow_html=True)