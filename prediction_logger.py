import json
import csv
import os
from datetime import datetime
from pathlib import Path

class PredictionLogger:
    """Logs predictions to JSON and CSV files for analytics"""
    
    def __init__(self, log_dir="prediction_logs"):
        self.log_dir = log_dir
        self.json_file = os.path.join(log_dir, "predictions.json")
        self.csv_file = os.path.join(log_dir, "predictions.csv")
        self._ensure_log_dir()
        
    def _ensure_log_dir(self):
        """Create log directory if it doesn't exist"""
        Path(self.log_dir).mkdir(exist_ok=True)
    
    def log_prediction(self, patient_data, prediction, probability, risk_level):
        """Log a prediction to both JSON and CSV"""
        timestamp = datetime.now().isoformat()
        
        log_entry = {
            "timestamp": timestamp,
            "patient_data": patient_data,
            "prediction": int(prediction),
            "probability": float(probability),
            "risk_level": risk_level
        }
        
        # Log to JSON
        self._append_json(log_entry)
        
        # Log to CSV
        self._append_csv(log_entry)
        
        return log_entry
    
    def _append_json(self, entry):
        """Append entry to JSON log file"""
        try:
            if os.path.exists(self.json_file):
                with open(self.json_file, 'r') as f:
                    data = json.load(f)
            else:
                data = []
            
            data.append(entry)
            
            with open(self.json_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error logging to JSON: {e}")
    
    def _append_csv(self, entry):
        """Append entry to CSV log file"""
        try:
            fieldnames = ["timestamp", "prediction", "probability", "risk_level", "age", "gender"]
            
            file_exists = os.path.exists(self.csv_file)
            
            with open(self.csv_file, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                if not file_exists:
                    writer.writeheader()
                
                row = {
                    "timestamp": entry["timestamp"],
                    "prediction": entry["prediction"],
                    "probability": entry["probability"],
                    "risk_level": entry["risk_level"],
                    "age": entry["patient_data"].get("age", ""),
                    "gender": entry["patient_data"].get("gender", "")
                }
                writer.writerow(row)
        except Exception as e:
            print(f"Error logging to CSV: {e}")
    
    def get_statistics(self):
        """Get prediction statistics"""
        try:
            if not os.path.exists(self.json_file):
                return None
            
            with open(self.json_file, 'r') as f:
                data = json.load(f)
            
            if not data:
                return None
            
            predictions = [entry["prediction"] for entry in data]
            probabilities = [entry["probability"] for entry in data]
            
            return {
                "total_predictions": len(data),
                "positive_cases": sum(predictions),
                "negative_cases": len(predictions) - sum(predictions),
                "avg_probability": sum(probabilities) / len(probabilities),
                "first_prediction": data[0]["timestamp"],
                "last_prediction": data[-1]["timestamp"]
            }
        except Exception as e:
            print(f"Error getting statistics: {e}")
            return None

# Global logger instance
logger = PredictionLogger()
