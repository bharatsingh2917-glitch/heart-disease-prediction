import pytest
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

def test_model_loaded():
    """Test if model is loaded correctly"""
    assert model is not None
    assert hasattr(model, 'predict')
    assert hasattr(model, 'predict_proba')

def test_model_input_shape():
    """Test if model accepts correct input shape"""
    # Model expects 13 features
    test_input = np.array([[50, 1, 0, 120, 0, 0, 1, 0, 0, 0, 0, 0, 0]])
    prediction = model.predict(test_input)
    assert len(prediction) == 1
    assert prediction[0] in [0, 1]

def test_model_probability_output():
    """Test if model returns valid probabilities"""
    test_input = np.array([[50, 1, 0, 120, 0, 0, 1, 0, 0, 0, 0, 0, 0]])
    probability = model.predict_proba(test_input)
    assert probability.shape == (1, 2)
    assert np.all(probability >= 0) and np.all(probability <= 1)
    assert np.isclose(probability.sum(), 1.0)

def test_model_batch_prediction():
    """Test if model can make batch predictions"""
    batch_input = np.array([
        [50, 1, 0, 120, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [40, 0, 1, 110, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [60, 1, 1, 130, 1, 0, 0, 0, 0, 0, 1, 0, 0]
    ])
    predictions = model.predict(batch_input)
    assert len(predictions) == 3
    assert all(p in [0, 1] for p in predictions)

def test_model_feature_count():
    """Test if model expects exactly 13 features"""
    # Should fail with wrong number of features
    wrong_input = np.array([[50, 1, 0]])  # Only 3 features
    with pytest.raises(ValueError):
        model.predict(wrong_input)

def test_model_consistency():
    """Test if model gives consistent predictions"""
    test_input = np.array([[55, 1, 0, 125, 0, 0, 1, 0, 0, 0, 0, 0, 0]])
    pred1 = model.predict(test_input)
    pred2 = model.predict(test_input)
    assert np.array_equal(pred1, pred2)

def test_prediction_range():
    """Test if predictions are binary"""
    for _ in range(10):
        test_input = np.random.randint(0, 100, size=(5, 13))
        predictions = model.predict(test_input)
        assert all(p in [0, 1] for p in predictions)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
