import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time
import plotly.graph_objects as go
from datetime import datetime

# Load the model
model = joblib.load('model.pkl')

# Custom title with heart
st.set_page_config(
    page_title="❤️ Elite Heart Disease Prediction", 
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
    <style>
        /* Main background */
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Header styling */
        .header-container {
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(255, 107, 107, 0.3);
            margin-bottom: 30px;
        }
        
        .header-title {
            font-size: 3.5em;
            font-weight: 900;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            margin: 0;
        }
        
        .header-subtitle {
            font-size: 1.3em;
            color: white;
            margin-top: 10px;
            opacity: 0.95;
        }
        
        /* Input section styling */
        .input-section {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin: 20px 0;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        /* Prediction result styling */
        .result-high-risk {
            background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
            padding: 30px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 32px rgba(255, 107, 107, 0.3);
        }
        
        .result-low-risk {
            background: linear-gradient(135deg, #56AB2F 0%, #A8E063 100%);
            padding: 30px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 32px rgba(168, 224, 99, 0.3);
        }
        
        .result-title {
            font-size: 2.5em;
            font-weight: bold;
            margin: 10px 0;
        }
        
        .result-probability {
            font-size: 1.8em;
            margin: 15px 0;
            font-weight: bold;
        }
        
        .result-message {
            font-size: 1.1em;
            margin-top: 15px;
            line-height: 1.6;
        }
        
        /* Button styling */
        .stButton > button {
            width: 100%;
            padding: 15px;
            font-size: 1.2em;
            font-weight: bold;
            border-radius: 10px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
            transition: transform 0.2s;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        }
        
        /* Sidebar styling */
        .sidebar-content {
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            margin: 10px 0;
        }
        
        /* Footer styling */
        .footer {
            text-align: center;
            padding: 30px;
            color: white;
            margin-top: 40px;
            border-top: 2px solid rgba(255, 255, 255, 0.3);
        }
    </style>
""", unsafe_allow_html=True)

# Beautiful header
st.markdown("""
    <div class='header-container'>
        <h1 class='header-title'>❤️ Elite Heart Disease Prediction System</h1>
        <p class='header-subtitle'>🫀 AI-Powered Cardiovascular Health Analysis 🫀</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar with model info
with st.sidebar:
    st.markdown("### 🏥 SYSTEM INFORMATION")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🎯 Accuracy", "88.33%")
    with col2:
        st.metric("📊 Training Data", "297")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🌳 Trees", "100")
    with col2:
        st.metric("📈 Features", "13")
    
    st.markdown("---")
    st.markdown("### ⚙️ MODEL SPECS")
    st.info("✅ Random Forest Classifier\n\n🌳 Ensemble Learning\n\n✅ Production Ready")
    
    st.markdown("---")
    if 'prediction_history' in st.session_state and st.session_state.prediction_history:
        st.markdown(f"### 📜 History ({len(st.session_state.prediction_history)})")
        for i, pred in enumerate(st.session_state.prediction_history[-3:], 1):
            risk = "HIGH" if pred['risk'] == 1 else "LOW"
            st.text(f"{i}. {risk} - {pred['prob']:.1%}")

# Welcome section
with st.expander("📖 About This System", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🏥 Overview
        
        Elite Heart Disease Prediction System uses machine learning to assess cardiovascular risk.
        
        ### 🎯 Features
        - 🤖 AI-Powered Analysis
        - 📊 Real-time Predictions
        - 💡 Personalized Insights
        - 🔍 Detailed Analysis
        """)
    with col2:
        st.markdown("""
        ### 📊 Performance
        
        **Accuracy:** 88.33% ⭐
        
        **Type:** Classification
        
        **Trained on:** 297 samples
        """)

# Input features section
st.markdown("<div class='input-section'>", unsafe_allow_html=True)
st.markdown("## 💓 Patient Medical Information")
st.markdown("*Enter accurate medical data for analysis*")

# Tabs for better organization
tab1, tab2, tab3 = st.tabs(["👤 Personal", "🫀 Cardiac", "🧬 Metabolic"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        age = st.slider('👤 Age (years)', 20, 100, 50)
    with col2:
        sex = st.selectbox('⚧ Sex', [0, 1], format_func=lambda x: '👩 Female' if x == 0 else '👨 Male')

with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        cp = st.selectbox('🤕 Chest Pain', [0, 1, 2, 3], 
                         format_func=lambda x: ['Typical', 'Atypical', 'Non-anginal', 'Asymptomatic'][x])
    with col2:
        thalach = st.slider('⚡ Max Heart Rate', 70, 220, 150)
    with col3:
        exang = st.selectbox('🏃 Exercise Angina', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        oldpeak = st.slider('📉 ST Depression', 0.0, 6.0, 1.0)
    with col2:
        slope = st.selectbox('📈 ST Slope', [0, 1, 2], format_func=lambda x: ['Up', 'Flat', 'Down'][x])
    with col3:
        ca = st.slider('🚊 Vessels', 0, 3, 0)
    
    col1, col2 = st.columns(2)
    with col1:
        thal = st.selectbox('🩺 Thalassemia', [1, 2, 3, 6, 7], 
                           format_func=lambda x: {1: 'Normal', 2: 'Fixed', 3: 'Reversible', 6: 'Normal', 7: 'Reversible'}[x])
    with col2:
        restecg = st.selectbox('📊 Resting ECG', [0, 1, 2], format_func=lambda x: ['Normal', 'Abnormal', 'LVH'][x])

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        trestbps = st.slider('🩸 Resting BP', 90, 200, 120)
    with col2:
        chol = st.slider('🧬 Cholesterol', 100, 600, 200)
    
    fbs = st.selectbox('🍬 Fasting Blood Sugar', [0, 1], format_func=lambda x: 'Normal' if x == 0 else 'High')

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Prediction buttons
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    predict_button = st.button('🔍 Comprehensive Analysis', use_container_width=True)

with col2:
    reset_button = st.button('🔄 Reset', use_container_width=True)

if reset_button:
    st.rerun()

# Initialize session state
if 'prediction_history' not in st.session_state:
    st.session_state.prediction_history = []

if predict_button:
    with st.spinner('🤖 Analyzing...'):
        time.sleep(1)
        
        features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        prediction = model.predict(features)[0]
        probs = model.predict_proba(features)[0]
        
        prob_disease = probs[1]
        prob_safe = probs[0]
        
        st.session_state.prediction_history.append({
            'timestamp': datetime.now().strftime("%H:%M"),
            'age': age,
            'risk': prediction,
            'prob': prob_disease
        })
    
    st.markdown("---")
    st.markdown("### 📊 ANALYSIS RESULTS")
    
    if prediction == 1:
        st.markdown(f"""
            <div class='result-high-risk'>
                <div class='result-title'>⚠️ HIGH CARDIOVASCULAR RISK ⚠️</div>
                <div class='result-probability'>Risk: {prob_disease:.1%} | Safe: {prob_safe:.1%}</div>
                <div class='result-message'>
                    🚨 Elevated risk detected<br>
                    💔 IMMEDIATE ACTION REQUIRED<br>
                    🏥 Schedule cardiology appointment
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class='result-low-risk'>
                <div class='result-title'>✅ LOW CARDIOVASCULAR RISK ✅</div>
                <div class='result-probability'>Risk: {prob_disease:.1%} | Safe: {prob_safe:.1%}</div>
                <div class='result-message'>
                    ✨ Good health indicators<br>
                    ❤️ MAINTAIN CURRENT LIFESTYLE<br>
                    💪 Continue healthy habits
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Risk gauge (Plotly - with error handling)
    st.markdown("### 🎯 RISK ASSESSMENT")
    try:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prob_disease * 100,
            title={'text': "Risk %"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#FF6B6B" if prediction == 1 else "#56AB2F"},
                'steps': [
                    {'range': [0, 30], 'color': "#A8E063"},
                    {'range': [30, 70], 'color': "#FFD700"},
                    {'range': [70, 100], 'color': "#FF6B6B"}
                ]
            }
        ))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.info(f"Risk Score: {prob_disease:.1%}")
    
    # Risk factors
    st.markdown("---")
    st.markdown("### 🎯 RISK FACTOR ANALYSIS")
    
    col1, col2 = st.columns(2)
    with col1:
        risk_count = sum([
            cp > 0,
            trestbps > 140,
            chol > 240,
            exang == 1,
            oldpeak > 2,
            age > 60
        ])
        st.write(f"**Risk Factors: {risk_count}/6**")
        
        if cp > 0:
            st.warning("🤕 Chest pain present")
        if trestbps > 140:
            st.warning("🩸 High blood pressure")
        if chol > 240:
            st.warning("🧬 High cholesterol")
        if exang == 1:
            st.warning("🏃 Exercise-induced angina")
        if oldpeak > 2:
            st.warning("📉 ST depression")
        if age > 60:
            st.warning("👴 Advanced age")
        
        if risk_count == 0:
            st.success("✅ No major risk factors!")
    
    with col2:
        st.markdown("#### 🏥 RECOMMENDATIONS")
        
        recs = []
        if prediction == 1:
            recs.append("🚨 Schedule immediate cardiology consultation")
        if chol > 240:
            recs.append("🥗 Reduce dietary cholesterol")
        if trestbps > 140:
            recs.append("🧂 Reduce sodium intake")
        if thalach < 100:
            recs.append("🏃 Increase aerobic exercise")
        if age > 60:
            recs.append("📅 Schedule annual cardiac screening")
        if not recs:
            recs.append("✅ Maintain current lifestyle")
            recs.append("💪 Continue regular exercise")
        
        for rec in recs:
            st.info(rec)
    
    # Comparative analysis
    st.markdown("---")
    st.markdown("### 📊 COMPARATIVE ANALYSIS")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        bp_diff = trestbps - 120
        st.metric("Blood Pressure", f"{trestbps} mm Hg", f"{bp_diff:+d}")
    with col2:
        chol_diff = chol - 200
        st.metric("Cholesterol", f"{chol} mg/dl", f"{chol_diff:+d}")
    with col3:
        hr_diff = thalach - 70
        st.metric("Heart Rate", f"{thalach} bpm", f"{hr_diff:+d}")

st.markdown("---")
st.markdown("""
    <div class='footer'>
        <p style='font-size: 0.9em; color: rgba(255,255,255,0.7);'>
            💊 For educational purposes. Always consult healthcare professionals. 🏥
        </p>
    </div>
""", unsafe_allow_html=True)