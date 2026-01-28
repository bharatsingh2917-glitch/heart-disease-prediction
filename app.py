import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time
from datetime import datetime
import csv
import io

# Load the model
model = joblib.load('model.pkl')

# Initialize session state
if 'prediction_history' not in st.session_state:
    st.session_state.prediction_history = []
if 'patient_data' not in st.session_state:
    st.session_state.patient_data = {}
if 'patients' not in st.session_state:
    st.session_state.patients = {}
if 'current_patient' not in st.session_state:
    st.session_state.current_patient = 'New Patient'
if 'doctor_notes' not in st.session_state:
    st.session_state.doctor_notes = {}
if 'health_goals' not in st.session_state:
    st.session_state.health_goals = []
if 'follow_ups' not in st.session_state:
    st.session_state.follow_ups = []

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
        <h1 class='header-title'>❤️ Heart Disease Prediction</h1>
        <p class='header-subtitle'>🫀 Advanced AI-Powered Health Assessment 🫀</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar with model info
with st.sidebar:
    st.markdown("### 📊 Model Information")
    st.metric("🎯 Model Accuracy", "88.33%", help="Accuracy on test set")
    st.metric("🤖 Algorithm", "Random Forest", help="Machine Learning Model")
    st.metric("🌳 Number of Trees", "100", help="Ensemble estimators")
    st.metric("📈 Test Set Size", "20%", help="Validation data split")
    
    st.markdown("---")
    st.markdown("### � Patient Management")
    
    # Patient selector
    if st.session_state.patients:
        patient_list = list(st.session_state.patients.keys())
        st.session_state.current_patient = st.selectbox("Select Patient", patient_list + ["New Patient"])
    else:
        st.session_state.current_patient = "New Patient"
    
    # Add new patient
    if st.session_state.current_patient == "New Patient":
        new_patient_name = st.text_input("Patient Name (optional)")
        if st.button("➕ Add New Patient Profile"):
            if new_patient_name:
                st.session_state.patients[new_patient_name] = {'predictions': [], 'notes': '', 'goals': []}
                st.session_state.current_patient = new_patient_name
                st.success(f"✅ Patient {new_patient_name} added!")
            else:
                st.warning("⚠️ Please enter a patient name")
    
    # Display current patient info
    if st.session_state.current_patient != "New Patient":
        st.write(f"**Current:** {st.session_state.current_patient}")
        if st.button("🗑️ Delete Patient"):
            del st.session_state.patients[st.session_state.current_patient]
            st.session_state.current_patient = "New Patient"
            st.success("Patient deleted!")
    
    st.markdown("---")
    st.markdown("### 📜 Prediction History")
    if st.session_state.prediction_history:
        st.write(f"**Total Predictions:** {len(st.session_state.prediction_history)}")
        with st.expander("View History"):
            for i, record in enumerate(st.session_state.prediction_history[-5:], 1):
                risk = "🔴 HIGH" if record['risk'] == 1 else "🟢 LOW"
                st.write(f"{i}. {risk} - {record['prob']:.1%} - {record['timestamp']}")
    else:
        st.write("No predictions yet")
    
    if st.button("🔄 Clear History"):
        st.session_state.prediction_history = []
        st.success("History cleared!")
    
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.info("""
    ✅ Enter accurate medical data for better predictions
    
    ⚠️ This is a screening tool only
    
    🏥 Always consult healthcare professionals
    """)

# Welcome section
with st.expander("📖 About This App", expanded=False):
    st.markdown("""
    🏥 **Welcome to the Heart Disease Prediction System**
    
    This cutting-edge application uses advanced machine learning to assess your heart health risk.
    
    **How it works:**
    - ✅ Enter your medical information
    - 🤖 Our AI model analyzes your data
    - 📊 Get instant risk assessment
    - 💡 Receive personalized insights
    
    **Model Performance:**
    - 🎯 **Accuracy: 88.33%** - Highly reliable predictions
    - 🌳 Trained on 297 patient samples
    - 📊 13 different health factors analyzed
    
    **Important:** This tool is for educational purposes only. Always consult qualified healthcare professionals.
    """)

# Dashboard Tab
st.markdown("---")
tab1, tab2, tab3, tab4 = st.tabs(["🩺 Prediction", "📊 Dashboard", "📝 Notes & Goals", "❓ Health Tips"])

with tab2:
    st.markdown("### 📊 Health Dashboard")
    
    if st.session_state.prediction_history:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📈 Total Predictions", len(st.session_state.prediction_history))
        with col2:
            high_risk_count = sum(1 for p in st.session_state.prediction_history if p['risk'] == 1)
            st.metric("🔴 High Risk", high_risk_count)
        with col3:
            low_risk_count = sum(1 for p in st.session_state.prediction_history if p['risk'] == 0)
            st.metric("🟢 Low Risk", low_risk_count)
        with col4:
            avg_age = np.mean([p['age'] for p in st.session_state.prediction_history])
            st.metric("👤 Avg Age", f"{avg_age:.0f}")
        
        # Risk trend
        st.markdown("#### 📈 Risk Trend Over Time")
        trend_data = pd.DataFrame(st.session_state.prediction_history)
        trend_data['risk_percentage'] = trend_data['prob'] * 100
        st.line_chart(trend_data[['risk_percentage']], use_container_width=True)
        
        # Statistics
        st.markdown("#### 📊 Statistics")
        col1, col2 = st.columns(2)
        with col1:
            risk_avg = np.mean([p['prob'] for p in st.session_state.prediction_history])
            st.write(f"**Average Risk Level:** {risk_avg:.1%}")
        with col2:
            risk_max = max([p['prob'] for p in st.session_state.prediction_history])
            st.write(f"**Maximum Risk:** {risk_max:.1%}")
    else:
        st.info("No prediction data yet. Run predictions to see the dashboard.")

with tab3:
    st.markdown("### 📝 Doctor's Notes & Health Goals")
    
    # Doctor's notes
    st.markdown("#### 🏥 Doctor's Notes")
    notes_key = st.session_state.current_patient if st.session_state.current_patient != "New Patient" else "temp_notes"
    
    if notes_key not in st.session_state.doctor_notes:
        st.session_state.doctor_notes[notes_key] = ""
    
    notes_input = st.text_area("Add doctor's notes or observations:", 
                                value=st.session_state.doctor_notes.get(notes_key, ""),
                                height=100)
    
    if st.button("💾 Save Notes"):
        st.session_state.doctor_notes[notes_key] = notes_input
        st.success("✅ Notes saved!")
    
    # Health goals
    st.markdown("#### 🎯 Health Goals")
    col1, col2 = st.columns([3, 1])
    with col1:
        goal_input = st.text_input("Add a health goal:", placeholder="e.g., Reduce cholesterol by 20%")
    with col2:
        if st.button("➕ Add Goal"):
            if goal_input:
                st.session_state.health_goals.append({'goal': goal_input, 'date': datetime.now().strftime("%Y-%m-%d")})
                st.success("✅ Goal added!")
    
    if st.session_state.health_goals:
        st.markdown("##### Your Goals:")
        for i, goal in enumerate(st.session_state.health_goals, 1):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"**{i}. {goal['goal']}** ({goal['date']})")
            with col2:
                if st.button(f"❌", key=f"goal_{i}"):
                    st.session_state.health_goals.pop(i-1)
                    st.rerun()

with tab4:
    st.markdown("### ❓ Health Tips & Education")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 💚 Heart Health Tips
        
        **Daily Habits:**
        - 🚶 Walk 30 minutes daily
        - 🥗 Eat more fruits & vegetables
        - 💧 Drink 8 glasses of water
        - 😴 Sleep 7-9 hours
        
        **Foods to Avoid:**
        - ❌ Trans fats
        - ❌ High sodium
        - ❌ Excess sugar
        - ❌ Processed meats
        """)
    
    with col2:
        st.markdown("""
        ### 📊 Risk Factors to Monitor
        
        **Critical Factors:**
        - 🩸 Blood Pressure > 140/90
        - 🧬 Cholesterol > 240
        - ⚡ Resting heart rate anomalies
        - 🤕 Chest pain symptoms
        
        **Prevention Tips:**
        - 🏃 Regular exercise
        - 🧘 Stress management
        - ⛔ Quit smoking
        - 📅 Regular check-ups
        """)
    
    # BMI Calculator
    st.markdown("---")
    st.markdown("### 📏 BMI Calculator")
    col1, col2 = st.columns(2)
    with col1:
        height_cm = st.number_input("Height (cm)", 100, 220, 170)
    with col2:
        weight_kg = st.number_input("Weight (kg)", 30, 200, 70)
    
    if height_cm > 0 and weight_kg > 0:
        bmi = weight_kg / ((height_cm / 100) ** 2)
        col1, col2 = st.columns(2)
        with col1:
            st.metric("BMI", f"{bmi:.1f}")
        with col2:
            if bmi < 18.5:
                st.info("Underweight")
            elif bmi < 25:
                st.success("Normal Weight")
            elif bmi < 30:
                st.warning("Overweight")
            else:
                st.error("Obese")

# Main prediction tab
with tab1:
    st.markdown("---")
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
    col1, col2, col3 = st.columns(3)
    with col1:
        prediction_button = st.button('🔍 Analyze Heart Health', use_container_width=True)
    with col2:
        reset_button = st.button('🔄 Reset Form', use_container_width=True)
    with col3:
        save_button = st.button('💾 Save Data', use_container_width=True)

    if reset_button:
        st.rerun()

    if save_button:
        st.session_state.patient_data = {
            'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps,
            'chol': chol, 'fbs': fbs, 'restecg': restecg, 'thalach': thalach,
            'exang': exang, 'oldpeak': oldpeak, 'slope': slope, 'ca': ca, 'thal': thal
        }
        st.success("✅ Patient data saved!")

    if prediction_button:
        # Show loading animation
        with st.spinner('🤖 AI is analyzing your data...'):
            time.sleep(1)
            
            features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            prediction = model.predict(features)[0]
            prob = model.predict_proba(features)[0]
            
            prob_no_disease = prob[0]
            prob_disease = prob[1]
            
            # Add to history
            st.session_state.prediction_history.append({
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M"),
                'age': age,
                'risk': prediction,
                'prob': prob_disease
            })
            
            # Calculate health score
            health_score = 100 * prob_no_disease
            risk_level = "🔴 CRITICAL" if prob_disease > 0.8 else ("🟠 HIGH" if prob_disease > 0.5 else ("🟡 MODERATE" if prob_disease > 0.3 else "🟢 LOW"))
        
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
        
        # Health Score Display
        st.markdown("---")
        st.markdown("### 🏥 Health Score & Risk Level")
        col_score1, col_score2, col_score3 = st.columns(3)
        with col_score1:
            st.metric("💚 Health Score", f"{health_score:.1f}/100")
        with col_score2:
            st.metric("⚠️ Risk Level", risk_level)
        with col_score3:
            st.metric("📊 Confidence", f"{max(prob_disease, prob_no_disease):.1%}")
        
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
        
        # Lifestyle Assessment
        st.markdown("---")
        st.markdown("### 🏃 Lifestyle Assessment")
        col_lifestyle1, col_lifestyle2 = st.columns(2)
        
        with col_lifestyle1:
            st.write("**Activity Level:**")
            if thalach < 100:
                st.warning("⬇️ Low activity - increase exercise")
            elif thalach < 130:
                st.info("⚠️ Moderate - room for improvement")
            else:
                st.success("✅ Good cardiovascular fitness")
        
        with col_lifestyle2:
            st.write("**Stress/Symptom Level:**")
            if exang == 1:
                st.warning("⬆️ Exercise-induced angina detected")
            else:
                st.success("✅ No exercise-induced symptoms")
        
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
        if oldpeak > 2:
            recommendations.append("💊 Consider cardiac stress management program")
        
        if not recommendations:
            recommendations.append("✅ Maintain your current healthy lifestyle!")
            recommendations.append("💪 Continue regular exercise and balanced diet")
            recommendations.append("🥗 Keep following healthy eating habits")
        
        for i, rec in enumerate(recommendations, 1):
            st.markdown(f"**{i}. {rec}**")
        
        # Export Results
        st.markdown("---")
        st.markdown("### 📥 Export Results")
        
        col_export1, col_export2 = st.columns(2)
        
        with col_export1:
            # CSV Download
            result_df = pd.DataFrame({
                'Parameter': ['Age', 'Sex', 'Heart Rate', 'Blood Pressure', 'Cholesterol', 'Risk Prediction', 'Risk Probability', 'Health Score'],
                'Value': [age, 'Male' if sex == 1 else 'Female', thalach, trestbps, chol, 'HIGH RISK' if prediction == 1 else 'LOW RISK', f'{prob_disease:.1%}', f'{health_score:.1f}']
            })
            csv_buffer = io.StringIO()
            result_df.to_csv(csv_buffer, index=False)
            csv_string = csv_buffer.getvalue()
            
            st.download_button(
                label="📊 Download Results (CSV)",
                data=csv_string,
                file_name=f"heart_prediction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
        
        with col_export2:
            if st.session_state.prediction_history:
                # History Download
                history_df = pd.DataFrame(st.session_state.prediction_history)
                csv_history = history_df.to_csv(index=False)
                
                st.download_button(
                    label="📜 Download History (CSV)",
                    data=csv_history,
                    file_name=f"prediction_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )

st.markdown("---")
st.markdown("""
    <div class='footer'>
        <p style='font-size: 0.9em; color: rgba(255,255,255,0.7);'>
            💊 For educational purposes. Always consult healthcare professionals. 🏥
        </p>
    </div>
""", unsafe_allow_html=True)