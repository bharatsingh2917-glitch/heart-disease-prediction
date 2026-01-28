import pandas as pd
import numpy as np
import joblib
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt

# Heart emoji styling
HEART_DIVIDER = "❤️" * 30

class AIHeartModelExplainer:
    """
    🫀 AI-Powered Heart Disease Model Explainer
    
    This class provides advanced insights and explanations about the heart disease prediction model,
    including feature importance, prediction analysis, and model interpretability.
    """
    
    def __init__(self, model_path='model.pkl', data_path='data/heart.csv'):
        """Initialize the explainer with model and data."""
        print(f"\n{HEART_DIVIDER}")
        print("🤖 AI MODEL EXPLAINER INITIALIZED 🤖")
        print(f"{HEART_DIVIDER}\n")
        
        self.model = joblib.load(model_path)
        
        # Load data
        self.data = pd.read_csv(data_path, header=None, names=[
            'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
        ])
        
        self.data = self.data.replace('?', pd.NA).dropna()
        self.X = self.data.drop('target', axis=1)
        self.y = self.data['target']
        
        self.feature_names = self.X.columns.tolist()
        
    def explain_features(self):
        """Explain what each feature represents and its importance."""
        print(f"\n{HEART_DIVIDER}")
        print("📊 FEATURE EXPLANATION 📊")
        print(f"{HEART_DIVIDER}\n")
        
        feature_descriptions = {
            'age': '👤 Age - Patient age in years',
            'sex': '⚧ Sex - 0=Female, 1=Male',
            'cp': '🤕 Chest Pain Type - 0-3 scale (Typical Angina to Asymptomatic)',
            'trestbps': '🩸 Resting Blood Pressure - in mm Hg',
            'chol': '🧬 Serum Cholesterol - in mg/dl',
            'fbs': '🍬 Fasting Blood Sugar - 0=<=120, 1=>120 mg/dl',
            'restecg': '📊 Resting ECG Results - 0-2 scale',
            'thalach': '⚡ Max Heart Rate Achieved - beats per minute',
            'exang': '🏃 Exercise Induced Angina - 0=No, 1=Yes',
            'oldpeak': '📉 ST Depression - induced by exercise',
            'slope': '📈 Slope of Peak ST Segment - 0-2 scale',
            'ca': '🚊 Number of Major Vessels - 0-3',
            'thal': '🩺 Thalassemia - 1-7 scale'
        }
        
        for feature, description in feature_descriptions.items():
            print(f"  {description}")
        
    def analyze_feature_importance(self):
        """Analyze and display feature importance from the model."""
        print(f"\n{HEART_DIVIDER}")
        print("🧠 AI FEATURE IMPORTANCE ANALYSIS 🧠")
        print(f"{HEART_DIVIDER}\n")
        
        # Get feature importance from the model
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1]
        
        print("📊 Top Features Contributing to Heart Disease Prediction:\n")
        for i in range(min(10, len(indices))):
            idx = indices[i]
            importance = importances[idx]
            bar = "█" * int(importance * 100)
            print(f"  {i+1}. {self.feature_names[idx]:15s} | {importance:6.2%} {bar}")
        
        return importances, indices
    
    def predict_with_explanation(self, features):
        """
        Make a prediction and provide detailed explanation.
        
        Args:
            features: numpy array of feature values
        """
        print(f"\n{HEART_DIVIDER}")
        print("🔮 AI PREDICTION WITH EXPLANATION 🔮")
        print(f"{HEART_DIVIDER}\n")
        
        prediction = self.model.predict(features)[0]
        probabilities = self.model.predict_proba(features)[0]
        
        prob_no_disease = probabilities[0]
        prob_disease = probabilities[1]
        
        print(f"💓 Prediction: {'HIGH RISK ⚠️' if prediction == 1 else 'LOW RISK ✅'}")
        print(f"❤️  Probability of Heart Disease: {prob_disease:.1%}")
        print(f"💚 Probability of No Disease: {prob_no_disease:.1%}")
        
        # Confidence analysis
        confidence = max(prob_disease, prob_no_disease)
        print(f"🎯 Model Confidence: {confidence:.1%}")
        
        if confidence < 0.6:
            print("   ⚠️  Low confidence - result should be verified with healthcare professional")
        elif confidence >= 0.85:
            print("   ✅ High confidence prediction")
        else:
            print("   🔍 Moderate confidence - worth investigating further")
        
        return prediction, probabilities
    
    def get_model_statistics(self):
        """Display comprehensive model statistics."""
        print(f"\n{HEART_DIVIDER}")
        print("📈 MODEL STATISTICS 📈")
        print(f"{HEART_DIVIDER}\n")
        
        print(f"  Total Samples: {len(self.data)}")
        print(f"  Healthy Cases: {(self.y == 0).sum()} ({(self.y == 0).sum()/len(self.y)*100:.1f}%)")
        print(f"  Heart Disease Cases: {(self.y == 1).sum()} ({(self.y == 1).sum()/len(self.y)*100:.1f}%)")
        print(f"  Number of Features: {len(self.feature_names)}")
        print(f"  Model Type: Random Forest Classifier")
        print(f"  Number of Trees: {len(self.model.estimators_)}")
    
    def generate_report(self):
        """Generate a comprehensive AI analysis report."""
        print("\n" + "="*70)
        print("=" * 15 + " 🫀 HEART DISEASE PREDICTION MODEL REPORT 🫀 " + "="*15)
        print("="*70)
        
        self.get_model_statistics()
        self.explain_features()
        importances, indices = self.analyze_feature_importance()
        
        print(f"\n{HEART_DIVIDER}")
        print("💡 AI INSIGHTS & RECOMMENDATIONS 💡")
        print(f"{HEART_DIVIDER}\n")
        
        top_feature = self.feature_names[indices[0]]
        print(f"  🎯 Most Important Factor: {top_feature}")
        print(f"     - This feature has the highest impact on predictions")
        print(f"\n  📋 Key Recommendations:")
        print(f"     - Regularly monitor top risk factors")
        print(f"     - Use this model as a screening tool only")
        print(f"     - Always consult healthcare professionals for diagnosis")
        print(f"     - Consider lifestyle modifications based on results")
        
        print(f"\n{HEART_DIVIDER}")
        print("✅ Report Generation Complete")
        print(f"{HEART_DIVIDER}\n")


# Example usage
if __name__ == "__main__":
    # Initialize the explainer
    explainer = AIHeartModelExplainer()
    
    # Generate full report
    explainer.generate_report()
    
    # Example: Make a prediction with explanation
    print("\n📝 EXAMPLE PREDICTION:")
    example_patient = np.array([[
        63,    # age
        1,     # sex (male)
        3,     # cp (asymptomatic)
        145,   # trestbps
        233,   # chol
        1,     # fbs
        0,     # restecg
        150,   # thalach
        0,     # exang
        2.3,   # oldpeak
        0,     # slope
        0,     # ca
        1      # thal
    ]])
    
    prediction, probs = explainer.predict_with_explanation(example_patient)
    
    print("\n" + "="*70)
    print("🫀 AI MODEL EXPLAINER COMPLETE 🫀")
    print("="*70 + "\n")
