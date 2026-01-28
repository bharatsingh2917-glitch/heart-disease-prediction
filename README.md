# Heart Disease Prediction App

## Problem Statement

Heart disease remains one of the leading causes of mortality worldwide, accounting for approximately 17.9 million deaths annually according to the World Health Organization. Early detection and risk assessment are crucial for preventing adverse outcomes, but traditional diagnostic methods often rely on manual interpretation of medical tests, which can be time-consuming, subjective, and prone to human error. 

This project addresses the need for an accessible, automated tool that leverages machine learning to predict heart disease risk based on patient demographic and clinical data. By providing a user-friendly web interface, the application empowers healthcare professionals and individuals to make informed decisions quickly, potentially reducing diagnostic delays and improving patient outcomes.

## SDG Alignment

This project aligns with **United Nations Sustainable Development Goal (SDG) 3: Good Health and Well-being**. SDG 3 aims to ensure healthy lives and promote well-being for all at all ages, with specific targets to reduce premature mortality from non-communicable diseases (including cardiovascular diseases) by one-third by 2030. The heart disease prediction app contributes to this goal by enabling early detection and risk assessment, supporting timely interventions, and promoting preventive healthcare.

## ✨ Features

### 🔐 **Authentication & Security**
- User login system with role-based access (Doctor, Patient, Admin)
- Demo mode for quick testing
- Session management for data privacy

### 🎨 **User Interface**
- Beautiful gradient-based design with heart emoji branding
- Light/Dark mode toggle for user preference
- Multi-tab interface for organized navigation
- Responsive design for desktop and mobile

### 🩺 **Prediction Engine**
- Input patient information through interactive forms
- Real-time heart disease risk prediction using Random Forest (88.33% accuracy)
- Comprehensive input validation with error handling
- Display risk levels (🔴 CRITICAL, 🟠 HIGH, 🟡 MODERATE, 🟢 LOW)
- Health score calculation (0-100 scale)

### 👥 **Patient Management**
- Create and manage patient profiles
- Save patient data for quick access
- Track patient history
- Personalized patient notes and follow-ups

### 📊 **Analytics Dashboard**
- Prediction history tracking with timestamps
- Risk trend analysis
- Statistical metrics (positive/negative cases, average probability)
- Export capabilities (CSV, PDF, JSON)
- Advanced analytics with prediction logging

### 📝 **Health Records**
- Doctor's notes storage and retrieval
- Health goals tracking and management
- Follow-up scheduling
- Patient data persistence

### 📄 **Report Generation**
- PDF report export with patient info and recommendations
- CSV export for raw data analysis
- JSON logging for data science workflows
- Comprehensive health recommendations

### 🏥 **Health Education**
- Interactive BMI calculator
- Heart disease risk factor education
- Lifestyle assessment tool
- Prevention tips and cardiac health guidelines

### 📈 **Data Logging & Analytics**
- Automatic prediction logging to JSON and CSV
- Prediction statistics and insights
- Aggregate analytics for trend analysis
- Audit trail for clinical validation

### 🌐 **Deployment Ready**
- Streamlit Cloud configuration included
- Docker-ready environment
- Environment variable support
- Scalable architecture

## AI Concepts and Algorithms

This project utilizes several key AI and machine learning concepts:

- **Supervised Learning**: The model is trained on labeled data to predict heart disease presence (binary classification).
- **Random Forest Algorithm**: An ensemble method that builds multiple decision trees and combines their predictions for improved accuracy and reduced overfitting.
- **Data Preprocessing**: Handling missing values, feature scaling (implicit in Random Forest), and data splitting for training/validation.
- **Model Evaluation**: Accuracy metric to assess performance on unseen test data.
- **Libraries Used**:
  - `scikit-learn`: For machine learning algorithms and evaluation
  - `pandas`: For data manipulation and analysis
  - `joblib`: For model serialization and loading

## Installation & Setup

### Local Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bharatsingh2917-glitch/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Train the model (optional, pre-trained model included):
   ```bash
   python model.py
   ```

### Running the Application

**Option 1: Standard App (Original)**
```bash
streamlit run app.py
```

**Option 2: Enhanced App (With All New Features)**
```bash
streamlit run app_enhanced.py
```

Open your browser to `http://localhost:8501`

### Default Credentials

The app includes a demo login system. Use these credentials to test:

| Role | Username | Password |
|------|----------|----------|
| Doctor | `doctor` | `doctor123` |
| Patient | `patient` | `patient123` |
| Admin | `admin` | `admin123` |

Or click "Demo Mode" to skip login.

### Running Tests

```bash
pytest test_model.py -v
```

### Cloud Deployment (Streamlit Cloud)

1. Push your repository to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io)
3. Click "New app" and select your repository
4. Point to `app_enhanced.py` as the main file
5. Deploy!

Alternatively, use the included `.streamlit/config.toml` for custom configuration.

## Project Structure

```
heart-disease-prediction/
├── app.py                      # Original Streamlit application
├── app_enhanced.py             # Enhanced app with all new features
├── model.py                    # ML model training and evaluation
├── auth.py                     # Authentication system
├── prediction_logger.py        # Prediction logging and analytics
├── pdf_report.py              # PDF report generation
├── ai_model_explainer.py      # Model explainability features
├── test_model.py              # Unit tests for model validation
├── credentials.yaml           # User credentials (auto-generated)
├── heart_disease_model.pkl    # Trained model
├── heart.csv                  # Dataset
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── .streamlit/
│   └── config.toml           # Streamlit configuration
└── prediction_logs/          # Auto-generated prediction logs
    ├── predictions.json      # JSON log of all predictions
    └── predictions.csv       # CSV log of all predictions
```

## Model Architecture & Performance

### Algorithm
- **Type**: Random Forest Classifier
- **Accuracy**: 88.33% on test set
- **Features**: 13 cardiac indicators
- **Training Set**: 80% of 297 patient samples
- **Test Set**: 20% of 297 patient samples

### Input Features

| Feature | Description | Range |
|---------|-------------|-------|
| Age | Patient age | 18-120 years |
| Gender | Male (1) or Female (0) | Binary |
| CP | Chest pain type | 0-3 |
| TRTBPS | Resting blood pressure | 80-250 mmHg |
| CHOL | Cholesterol level | 0-600 mg/dL |
| FBS | Fasting blood sugar > 120 | Binary |
| RESTECG | Resting ECG result | 0-2 |
| THALACHH | Max heart rate achieved | 40-220 bpm |
| EXNG | Exercise-induced angina | Binary |
| OLDPEAK | ST depression | 0-10 |
| SLP | Slope of ST segment | 0-2 |
| CAA | Major vessels (0-4) | 0-4 |
| THALL | Thalassemia type | 0-3 |

### How It Works

1. **Data Preprocessing**: Input validation and normalization
2. **Feature Engineering**: 13 cardiac indicators processed
3. **Model Prediction**: Random Forest ensemble voting
4. **Risk Calculation**: Probability-based risk categorization
5. **Health Score**: Composite score from 0-100
6. **Recommendations**: Personalized health guidance

## Advanced Features

### 🔐 Authentication System
- Multi-user support with role-based access
- Credentials stored in YAML format
- Session management
- Auto-generated default credentials

### 📊 Prediction Logging
- Automatic logging to JSON and CSV
- Timestamp tracking
- Statistical aggregation
- Audit trail capabilities

### 📄 PDF Report Generation
- Professional report formatting
- Patient information section
- Prediction results display
- Health recommendations
- Disclaimer for clinical purposes

### 🧪 Unit Testing
- Model validation tests
- Input/output shape verification
- Batch prediction testing
- Consistency checks

### 🌐 Streamlit Cloud Ready
- Pre-configured `.streamlit/config.toml`
- Custom theme with heart disease colors
- Deployment instructions included
- Environment variable support

### 💾 Data Persistence
- Session state management
- Patient profile storage
- Prediction history tracking
- Multi-session data retention

### 📈 Analytics Engine
- Prediction statistics calculation
- Risk distribution analysis
- Temporal tracking
- Exportable metrics

## API Reference

### prediction_logger.py

```python
from prediction_logger import logger

# Log a prediction
log_entry = logger.log_prediction(
    patient_data={"age": 50, "gender": 1, ...},
    prediction=1,
    probability=0.75,
    risk_level="🟠 HIGH"
)

# Get statistics
stats = logger.get_statistics()
# Returns: {
#   'total_predictions': 100,
#   'positive_cases': 25,
#   'negative_cases': 75,
#   'avg_probability': 0.45,
#   'first_prediction': '2024-01-28T10:00:00',
#   'last_prediction': '2024-01-28T15:30:00'
# }
```

### pdf_report.py

```python
from pdf_report import pdf_generator

# Generate PDF report
pdf_buffer = pdf_generator.generate_prediction_report(
    patient_name="John Doe",
    patient_data={...},
    prediction=1,
    probability=0.75,
    risk_level="🟠 HIGH"
)

# Use pdf_buffer with st.download_button or save to file
```

### auth.py

```python
from auth import auth

# Authenticate user
success, user = auth.authenticate("doctor", "doctor123")
# Returns: (True, {'name': 'Dr. Heart', 'role': 'Doctor'})

# Check if logged in
if auth.is_logged_in():
    auth.logout()
```

## Environment Variables

Create a `.env` file (optional):

```
STREAMLIT_SERVER_PORT=8501
STREAMLIT_LOGGER_LEVEL=info
STREAMLIT_CLIENT_SHOW_ERROR_DETAILS=true
```

## Troubleshooting

### Model Not Found Error
```bash
# Retrain the model
python model.py
```

### Credentials Not Loading
```bash
# Reset credentials (will generate defaults)
rm credentials.yaml
# Restart the app
```

### Port Already in Use
```bash
# Use a different port
streamlit run app_enhanced.py --server.port=8502
```

### Dependencies Installation Issues
```bash
# Upgrade pip
pip install --upgrade pip

# Clear pip cache
pip cache purge

# Reinstall requirements
pip install -r requirements.txt --no-cache-dir
```

## Performance Optimization

- **Model Caching**: Model is cached after first load
- **Session State**: Patient data persists across interactions
- **Lazy Loading**: Features load only when accessed
- **Efficient Predictions**: Single predictions take ~50ms

## Security Considerations

⚠️ **Important**: This app is for educational and research purposes.

- Change default credentials before deployment
- Use HTTPS in production
- Implement proper access controls
- Regular security audits recommended
- Comply with healthcare data regulations (HIPAA, GDPR, etc.)
- Never use this as sole diagnostic tool

## Dataset Information

- **Source**: Cleveland Heart Disease dataset (UCI ML Repository)
- **Samples**: 297 patient records
- **Features**: 13 cardiac health indicators
- **Missing Values**: Removed during preprocessing
- **Target Variable**: Heart disease presence (binary)

## Performance Metrics

| Metric | Score |
|--------|-------|
| Accuracy | 88.33% |
| Precision | ~85% |
| Recall | ~88% |
| F1-Score | ~86% |

## Conclusion

This heart disease prediction app demonstrates the practical application of machine learning in healthcare. By achieving 88.33% accuracy, the model provides a reliable tool for initial risk assessment.

### Key Achievements
- ✅ Comprehensive ML pipeline with 13 features
- ✅ Multi-tab Streamlit interface
- ✅ User authentication system
- ✅ PDF and CSV export capabilities
- ✅ Prediction logging and analytics
- ✅ Health education resources
- ✅ Deployment-ready configuration
- ✅ Unit tests and validation
- ✅ Alignment with SDG 3

### Future Enhancements
- Integration with electronic health records (EHR)
- Advanced model explainability (SHAP, LIME)
- Mobile app development
- Real-time alert system
- Multi-language support
- Integration with wearable devices
- Telemedicine integration
- Clinical trial validation

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**⚠️ Medical Disclaimer**: This application is for educational and informational purposes only. It should not be used for self-diagnosis or self-treatment of medical conditions. Always consult with a qualified healthcare professional for medical advice, diagnosis, or treatment.