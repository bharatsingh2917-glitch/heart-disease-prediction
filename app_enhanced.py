import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time
from datetime import datetime
import csv
import io
import yaml
import os
from auth import auth
from prediction_logger import logger
from pdf_report import pdf_generator

# Load the model
model = joblib.load('model.pkl')

# Page configuration
st.set_page_config(
    page_title="❤️ Heart Disease Prediction", 
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'user_logged_in' not in st.session_state:
    st.session_state.user_logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'user_role' not in st.session_state:
    st.session_state.user_role = None
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
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

# Theme colors
def get_theme():
    """Get color theme based on dark mode setting"""
    if st.session_state.dark_mode:
        return {
            'primary': '#E74C3C',
            'bg': '#1e1e1e',
            'secondary_bg': '#2d2d2d',
            'text': '#ffffff',
            'text_secondary': '#b0b0b0'
        }
    else:
        return {
            'primary': '#E74C3C',
            'bg': '#ffffff',
            'secondary_bg': '#f0f2f6',
            'text': '#262730',
            'text_secondary': '#808080'
        }

# Apply custom CSS
theme = get_theme()
st.markdown(f"""
    <style>
        /* Main background */
        .stApp {{
            background: linear-gradient(135deg, #F5F9FF 0%, #FFFFFF 100%);
        }}
        
        /* Header styling */
        .header-container {{
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(255, 107, 107, 0.3);
            margin-bottom: 30px;
        }}
        
        .header-title {{
            font-size: 3.5em;
            font-weight: 900;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            margin: 0;
        }}
        
        .header-subtitle {{
            font-size: 1.3em;
            color: white;
            margin-top: 10px;
            opacity: 0.95;
        }}
        
        /* Input section styling */
        .input-section {{
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            margin: 20px 0;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }}
        
        /* Prediction result styling */
        .result-high-risk {{
            background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
            padding: 30px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 32px rgba(255, 107, 107, 0.3);
        }}
        
        .result-low-risk {{
            background: linear-gradient(135deg, #56AB2F 0%, #A8E063 100%);
            padding: 30px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 8px 32px rgba(168, 224, 99, 0.3);
        }}
        
        .result-title {{
            font-size: 2.5em;
            font-weight: bold;
            margin: 0;
            margin-bottom: 15px;
        }}
        
        .result-subtitle {{
            font-size: 1.2em;
            margin: 10px 0;
            opacity: 0.9;
        }}
        
        /* Stats box */
        .stat-box {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 10px 0;
        }}
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        }}
        
        .sidebar-item {{
            color: white;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
        }}
    </style>
""", unsafe_allow_html=True)

# Login screen
def login_page():
    """Display login page"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
            <div style='text-align: center; padding: 50px 0;'>
                <h1 style='color: #E74C3C; font-size: 3em;'>❤️</h1>
                <h2 style='color: #333;'>Heart Disease Prediction</h2>
                <p style='color: #666; font-size: 1.1em;'>Early Detection Saves Lives</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        username = st.text_input("👤 Username", key="login_username")
        password = st.text_input("🔒 Password", type="password", key="login_password")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🔓 Login", use_container_width=True):
                success, user = auth.authenticate(username, password)
                if success:
                    st.session_state.user_logged_in = True
                    st.session_state.current_user = user.get('name', username)
                    st.session_state.user_role = user.get('role', 'User')
                    st.success("✅ Login successful!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")
        
        with col_b:
            if st.button("👁️ Demo Mode", use_container_width=True):
                st.session_state.user_logged_in = True
                st.session_state.current_user = "Demo User"
                st.session_state.user_role = "Patient"
                st.success("✅ Entered demo mode!")
                time.sleep(1)
                st.rerun()
        
        st.markdown("---")
        
        with st.expander("📋 Demo Credentials"):
            st.info("""
            **Doctor Account:**
            - Username: `doctor`
            - Password: `doctor123`
            
            **Patient Account:**
            - Username: `patient`
            - Password: `patient123`
            
            **Admin Account:**
            - Username: `admin`
            - Password: `admin123`
            """)

# Validate input function
def validate_input(age, gender, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall):
    """Validate user inputs with comprehensive checks"""
    errors = []
    
    if age < 18 or age > 120:
        errors.append("Age must be between 18 and 120 years")
    
    if trtbps < 80 or trtbps > 250:
        errors.append("Blood Pressure must be between 80-250 mmHg")
    
    if chol < 0 or chol > 600:
        errors.append("Cholesterol must be between 0-600 mg/dL")
    
    if thalachh < 40 or thalachh > 220:
        errors.append("Max Heart Rate must be between 40-220 bpm")
    
    if oldpeak < 0 or oldpeak > 10:
        errors.append("ST Depression must be between 0-10")
    
    if caa < 0 or caa > 4:
        errors.append("Major Vessels must be between 0-4")
    
    return errors

# Main app
def main_app():
    """Main application"""
    # Header
    st.markdown("""
        <div class="header-container">
            <p class="header-title">❤️ Heart Disease Prediction System</p>
            <p class="header-subtitle">AI-Powered Early Detection & Health Management</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.current_user}")
        st.markdown(f"**Role:** {st.session_state.user_role}")
        
        st.markdown("---")
        
        # Dark mode toggle
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Theme:**")
        with col2:
            if st.button("🌙 Dark Mode" if not st.session_state.dark_mode else "☀️ Light Mode"):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()
        
        st.markdown("---")
        
        st.markdown("### 📊 Model Information")
        st.info("""
        **Algorithm:** Random Forest Classifier
        **Accuracy:** 88.33%
        **Features:** 13 cardiac indicators
        **Status:** ✅ Trained & Ready
        """)
        
        st.markdown("---")
        
        # Quick stats
        st.markdown("### 📈 Session Statistics")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Predictions", len(st.session_state.prediction_history))
        with col2:
            st.metric("Patients", len(st.session_state.patients))
        
        st.markdown("---")
        
        # Prediction history preview
        if st.session_state.prediction_history:
            st.markdown("### 📝 Recent Predictions")
            for i, pred in enumerate(st.session_state.prediction_history[-3:]):
                risk = "🔴 HIGH RISK" if pred['prediction'] == 1 else "🟢 LOW RISK"
                st.markdown(f"{i+1}. {risk} ({pred['timestamp']})")
        
        st.markdown("---")
        
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.user_logged_in = False
            st.session_state.current_user = None
            st.session_state.user_role = None
            st.rerun()
    
    # Main tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🩺 Prediction", "📊 Dashboard", "📝 Notes & Goals", "❓ Health Tips", "⚙️ Analytics"])
    
    # TAB 1: Prediction
    with tab1:
        st.markdown("### Enter Patient Health Information")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.number_input("👤 Age (years)", min_value=18, max_value=120, value=50)
            gender = st.radio("👫 Gender", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
            cp = st.selectbox("🫀 Chest Pain Type", options=[0, 1, 2, 3], 
                            format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"][x])
            trtbps = st.number_input("📊 Resting Blood Pressure (mmHg)", min_value=80, max_value=250, value=120)
            exng = st.radio("💪 Exercise-Induced Angina", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        
        with col2:
            chol = st.number_input("🧬 Cholesterol (mg/dL)", min_value=0, max_value=600, value=200)
            fbs = st.radio("🩸 Fasting Blood Sugar > 120", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
            restecg = st.selectbox("📈 Resting ECG", options=[0, 1, 2], 
                                  format_func=lambda x: ["Normal", "ST-T Abnormality", "LV Hypertrophy"][x])
            thalachh = st.number_input("❤️ Max Heart Rate Achieved", min_value=40, max_value=220, value=150)
            oldpeak = st.number_input("📉 ST Depression (induced by exercise)", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
        
        with col3:
            caa = st.selectbox("🩻 Major Vessels", options=[0, 1, 2, 3, 4], value=0)
            thall = st.selectbox("🧪 Thalassemia", options=[0, 1, 2, 3], 
                                format_func=lambda x: ["Normal", "Fixed Defect", "Reversible Defect", "Unknown"][x])
            slp = st.selectbox("📊 Slope of ST Segment", options=[0, 1, 2], 
                             format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x])
            st.write("")
            st.write("")
        
        # Validation
        errors = validate_input(age, gender, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall)
        
        if errors:
            for error in errors:
                st.warning(f"⚠️ {error}")
        
        # Patient name (optional)
        patient_name = st.text_input("Patient Name (optional)", value=st.session_state.current_patient if st.session_state.current_patient != 'New Patient' else "")
        
        # Save as patient
        if st.button("💾 Save as Patient Profile"):
            if patient_name and patient_name != 'New Patient':
                st.session_state.patients[patient_name] = {
                    'age': age, 'gender': gender, 'cp': cp, 'trtbps': trtbps,
                    'chol': chol, 'fbs': fbs, 'restecg': restecg, 'thalachh': thalachh,
                    'exng': exng, 'oldpeak': oldpeak, 'slp': slp, 'caa': caa, 'thall': thall
                }
                st.session_state.current_patient = patient_name
                st.success(f"✅ Patient profile '{patient_name}' saved!")
        
        # Predict button
        if st.button("🔮 Make Prediction", use_container_width=True):
            if not errors:
                # Prepare input
                input_data = np.array([[age, gender, cp, trtbps, chol, fbs, restecg, 
                                       thalachh, exng, oldpeak, slp, caa, thall]])
                
                # Make prediction
                prediction = model.predict(input_data)[0]
                probability = model.predict_proba(input_data)[0]
                
                # Calculate health score
                health_score = max(0, 100 - (prediction * 50) - (probability[1] * 50))
                
                # Determine risk level
                if probability[1] >= 0.8:
                    risk_level = "🔴 CRITICAL"
                elif probability[1] >= 0.6:
                    risk_level = "🟠 HIGH"
                elif probability[1] >= 0.4:
                    risk_level = "🟡 MODERATE"
                else:
                    risk_level = "🟢 LOW"
                
                # Log prediction
                patient_data = {
                    'age': age, 'gender': gender, 'cp': cp, 'trtbps': trtbps,
                    'chol': chol, 'fbs': fbs, 'restecg': restecg, 'thalachh': thalachh,
                    'exng': exng, 'oldpeak': oldpeak, 'slp': slp, 'caa': caa, 'thall': thall
                }
                
                logger.log_prediction(patient_data, prediction, probability[1], risk_level)
                
                # Store in history
                st.session_state.prediction_history.append({
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'patient': patient_name if patient_name else "Unnamed",
                    'prediction': prediction,
                    'probability': probability[1],
                    'health_score': health_score,
                    'risk_level': risk_level
                })
                
                # Display results
                st.markdown("---")
                
                if prediction == 1:
                    st.markdown(f"""
                        <div class="result-high-risk">
                            <p class="result-title">⚠️ HEART DISEASE DETECTED</p>
                            <p class="result-subtitle">Probability: {probability[1]*100:.2f}%</p>
                            <p class="result-subtitle">Risk Level: {risk_level}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.warning("""
                    **IMPORTANT:** This prediction suggests elevated risk.
                    - Consult a cardiologist immediately
                    - Do not delay medical evaluation
                    - This is not a clinical diagnosis
                    """)
                else:
                    st.markdown(f"""
                        <div class="result-low-risk">
                            <p class="result-title">✅ LOW RISK</p>
                            <p class="result-subtitle">Probability: {probability[1]*100:.2f}%</p>
                            <p class="result-subtitle">Health Score: {health_score:.1f}/100</p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.success("""
                    **POSITIVE NEWS:** Current indicators suggest lower risk.
                    - Maintain healthy lifestyle
                    - Regular check-ups recommended
                    - Continue preventive measures
                    """)
                
                # Export options
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    # CSV export
                    csv_data = f"Age,{age}\nGender,{['Female', 'Male'][gender]}\nChest Pain,{cp}\nBP,{trtbps}\nChol,{chol}\nPrediction,{['Low Risk', 'High Risk'][prediction]}\nProbability,{probability[1]:.2f}\n"
                    st.download_button("📥 Download CSV", csv_data, "prediction.csv", "text/csv")
                
                with col2:
                    # PDF export
                    pdf_buffer = pdf_generator.generate_prediction_report(
                        patient_name if patient_name else "Patient",
                        patient_data,
                        prediction,
                        probability[1],
                        risk_level
                    )
                    st.download_button("📄 Download PDF", pdf_buffer, "prediction_report.pdf", "application/pdf")
                
                with col3:
                    st.info(f"Health Score: **{health_score:.1f}**")
    
    # TAB 2: Dashboard
    with tab2:
        st.markdown("### 📊 Analytics Dashboard")
        
        if not st.session_state.prediction_history:
            st.info("No predictions yet. Make a prediction to see analytics!")
        else:
            col1, col2, col3, col4 = st.columns(4)
            
            predictions = [p['prediction'] for p in st.session_state.prediction_history]
            probabilities = [p['probability'] for p in st.session_state.prediction_history]
            
            with col1:
                st.metric("Total Predictions", len(predictions))
            with col2:
                st.metric("High Risk Cases", sum(predictions))
            with col3:
                st.metric("Low Risk Cases", len(predictions) - sum(predictions))
            with col4:
                st.metric("Avg Probability", f"{np.mean(probabilities)*100:.1f}%")
            
            # Prediction history table
            st.markdown("### 📈 Prediction History")
            history_df = pd.DataFrame(st.session_state.prediction_history)
            st.dataframe(history_df, use_container_width=True)
            
            # Export full history
            csv_buffer = io.StringIO()
            history_df.to_csv(csv_buffer, index=False)
            st.download_button("📥 Export History (CSV)", csv_buffer.getvalue(), "history.csv", "text/csv")
    
    # TAB 3: Notes & Goals
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📝 Doctor's Notes")
            selected_patient = st.selectbox("Select Patient", 
                                           options=list(st.session_state.patients.keys()) + ["New Note"],
                                           key="doctor_note_patient")
            
            notes = st.text_area("Add Doctor's Notes", height=150, 
                               value=st.session_state.doctor_notes.get(selected_patient, ""))
            
            if st.button("💾 Save Notes"):
                st.session_state.doctor_notes[selected_patient] = notes
                st.success("✅ Notes saved!")
        
        with col2:
            st.markdown("### 🎯 Health Goals")
            new_goal = st.text_input("Add a new health goal")
            
            if st.button("➕ Add Goal"):
                if new_goal:
                    st.session_state.health_goals.append({
                        'goal': new_goal,
                        'date': datetime.now().strftime("%Y-%m-%d"),
                        'completed': False
                    })
                    st.success("✅ Goal added!")
            
            st.markdown("#### Current Goals")
            for i, goal in enumerate(st.session_state.health_goals):
                col_a, col_b = st.columns([0.8, 0.2])
                with col_a:
                    completed = st.checkbox(goal['goal'], value=goal['completed'], key=f"goal_{i}")
                    st.session_state.health_goals[i]['completed'] = completed
                with col_b:
                    if st.button("🗑️", key=f"del_goal_{i}"):
                        st.session_state.health_goals.pop(i)
                        st.rerun()
    
    # TAB 4: Health Tips
    with tab4:
        st.markdown("### ❓ Heart Health Education")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🫀 Heart Disease Risk Factors")
            st.info("""
            **Major Risk Factors:**
            - High Blood Pressure
            - High Cholesterol
            - Smoking
            - Diabetes
            - Obesity
            - Physical Inactivity
            - Unhealthy Diet
            - Excessive Alcohol
            - Stress
            - Family History
            """)
            
            st.markdown("#### 💪 Prevention Tips")
            st.success("""
            - Exercise 150 min/week
            - Eat more fruits & vegetables
            - Reduce sodium intake
            - Avoid smoking
            - Manage stress
            - Maintain healthy weight
            - Regular health check-ups
            - Monitor cholesterol & BP
            """)
        
        with col2:
            st.markdown("#### 📏 BMI Calculator")
            weight = st.number_input("Weight (kg)", min_value=20, max_value=300, value=70)
            height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
            
            if height > 0:
                bmi = weight / ((height/100) ** 2)
                
                if bmi < 18.5:
                    category = "Underweight"
                    color = "🔵"
                elif bmi < 25:
                    category = "Normal Weight"
                    color = "🟢"
                elif bmi < 30:
                    category = "Overweight"
                    color = "🟡"
                else:
                    category = "Obese"
                    color = "🔴"
                
                st.metric("BMI", f"{bmi:.1f}", f"{color} {category}")
            
            st.markdown("#### 🫁 Lifestyle Assessment")
            smoking = st.radio("Do you smoke?", options=["Never", "Former", "Current"])
            exercise = st.radio("Exercise frequency", options=["Never", "1-2x/week", "3-4x/week", "5+x/week"])
            diet = st.radio("Diet quality", options=["Poor", "Fair", "Good", "Excellent"])
            
            if st.button("📊 Get Recommendations"):
                st.info("""
                Based on your inputs:
                - Smoking status affects heart health significantly
                - Increase exercise to at least 3-4x per week
                - Focus on Mediterranean diet
                - Schedule regular health check-ups
                """)
    
    # TAB 5: Analytics
    with tab5:
        st.markdown("### ⚙️ Advanced Analytics")
        
        stats = logger.get_statistics()
        
        if stats:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Logged Predictions", stats['total_predictions'])
            with col2:
                st.metric("Positive Cases", stats['positive_cases'])
            with col3:
                st.metric("Negative Cases", stats['negative_cases'])
            
            st.markdown("---")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Average Probability", f"{stats['avg_probability']*100:.1f}%")
            
            with col2:
                st.metric("Prediction Rate", f"{stats['positive_cases']/max(1, stats['total_predictions'])*100:.1f}%")
            
            st.info("""
            **Prediction Logs:**
            - First Prediction: """ + stats['first_prediction'] + """
            - Last Prediction: """ + stats['last_prediction'] + """
            """)
        else:
            st.info("No prediction logs available yet.")

# Main execution
if __name__ == "__main__":
    if not st.session_state.user_logged_in:
        login_page()
    else:
        main_app()
