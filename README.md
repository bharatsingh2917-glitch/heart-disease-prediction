# Heart Disease Prediction App

## Problem Statement

Heart disease remains one of the leading causes of mortality worldwide, accounting for approximately 17.9 million deaths annually according to the World Health Organization. Early detection and risk assessment are crucial for preventing adverse outcomes, but traditional diagnostic methods often rely on manual interpretation of medical tests, which can be time-consuming, subjective, and prone to human error. 

This project addresses the need for an accessible, automated tool that leverages machine learning to predict heart disease risk based on patient demographic and clinical data. By providing a user-friendly web interface, the application empowers healthcare professionals and individuals to make informed decisions quickly, potentially reducing diagnostic delays and improving patient outcomes.

## SDG Alignment

This project aligns with **United Nations Sustainable Development Goal (SDG) 3: Good Health and Well-being**. SDG 3 aims to ensure healthy lives and promote well-being for all at all ages, with specific targets to reduce premature mortality from non-communicable diseases (including cardiovascular diseases) by one-third by 2030. The heart disease prediction app contributes to this goal by enabling early detection and risk assessment, supporting timely interventions, and promoting preventive healthcare.

## Features

- Input patient information through an interactive web interface
- Predict heart disease risk using a Random Forest classifier
- Display prediction probability

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

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bharatsingh2917-glitch/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (optional, model is already trained):
   ```bash
   python model.py
   ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

Open your browser to `http://localhost:8501` to use the app.

## Dataset

The model is trained on the Cleveland Heart Disease dataset from the UCI Machine Learning Repository.

## Model

- Algorithm: Random Forest Classifier
- Accuracy: ~88% on test set

## Working of the Model

The heart disease prediction model operates through the following steps:

1. **Data Acquisition and Preprocessing**:
   - The Cleveland Heart Disease dataset is loaded from a CSV file.
   - Missing values (marked as '?') are removed to ensure data quality.
   - The target variable is binarized (0 for no disease, 1 for disease presence).

2. **Feature Selection**:
   - 13 clinical features are used as input variables, including age, sex, chest pain type, blood pressure, cholesterol levels, and more.

3. **Model Training**:
   - The dataset is split into training (80%) and testing (20%) sets.
   - A Random Forest classifier with 100 decision trees is trained on the training data.
   - The model learns patterns in the data to predict heart disease risk.

4. **Prediction and Evaluation**:
   - The trained model is evaluated on the test set, achieving approximately 88% accuracy.
   - For new patient data, the model outputs a probability score and binary prediction (high/low risk).

5. **Deployment**:
   - The model is serialized using joblib and loaded in the Streamlit app for real-time predictions.

## Conclusion

This heart disease prediction app demonstrates the practical application of machine learning in healthcare. By achieving 88% accuracy on the test set, the model provides a reliable tool for initial risk assessment. The user-friendly Streamlit interface makes it accessible to both medical professionals and individuals.

Key achievements include:
- Successful implementation of a supervised learning pipeline
- Integration of data preprocessing, model training, and web deployment
- Alignment with SDG 3 for global health improvement

Future improvements could involve:
- Incorporating larger, more diverse datasets
- Exploring advanced algorithms like neural networks
- Adding explainability features (e.g., SHAP values) for model interpretability
- Clinical validation and integration with electronic health records

## Acknowledgement

- **Dataset**: Cleveland Heart Disease dataset from the UCI Machine Learning Repository (https://archive.ics.uci.edu/dataset/45/heart+disease)
- **Libraries**: scikit-learn, pandas, numpy, matplotlib, joblib, Streamlit
- **Inspiration**: Open-source machine learning community and healthcare AI initiatives