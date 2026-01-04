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

- Input patient information through an interactive web interface
- Predict heart disease risk using a Random Forest classifier
- Display prediction probability

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