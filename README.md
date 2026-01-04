# Heart Disease Prediction App

This is a web application built with Streamlit that predicts the risk of heart disease based on patient data using a machine learning model trained on the Cleveland Heart Disease dataset.

## Features

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