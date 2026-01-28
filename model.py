import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Beautiful heart ASCII art
HEART_BANNER = """
    ❤️  ❤️  ❤️  HEART DISEASE PREDICTION MODEL  ❤️  ❤️  ❤️
    
       ♥ Training with Love and Science ♥
"""

print(HEART_BANNER)

# Load data
print("❤️  Loading heart disease data...")
data = pd.read_csv('data/heart.csv', header=None, names=[
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
])

# Preprocess
print("💓 Preprocessing data...")
data = data.replace('?', pd.NA).dropna()
data['target'] = data['target'].apply(lambda x: 0 if x == 0 else 1)

# Features and target
X = data.drop('target', axis=1)
y = data['target']

# Split
print("🫀 Splitting data into training and test sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
print("💪 Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
print("📊 Evaluating model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n" + "="*60)
print(f"✨ Model Training Complete! ✨")
print(f"❤️  Accuracy: {accuracy:.2%}")
print("="*60)

# Save model
print("💾 Saving model...")
joblib.dump(model, 'model.pkl')
print("✅ Model saved as 'model.pkl'!\n")