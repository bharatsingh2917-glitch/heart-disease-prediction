# Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the App
```bash
streamlit run app_enhanced.py
```

### 3. Login
- **Demo User**: Click "Demo Mode"
- **Doctor**: username `doctor` / password `doctor123`
- **Patient**: username `patient` / password `patient123`

### 4. Make a Prediction
- Fill in patient health information
- Click "🔮 Make Prediction"
- View results and export as PDF/CSV

---

## 🎯 Key Features

| Feature | Shortcut | What It Does |
|---------|----------|-------------|
| Prediction | Tab 1 | Enter patient data & get heart disease risk |
| Dashboard | Tab 2 | View analytics & prediction history |
| Notes | Tab 3 | Store doctor notes & health goals |
| Education | Tab 4 | Learn about heart health & BMI calculator |
| Analytics | Tab 5 | Advanced statistics & logging |

---

## 📊 Tabs Explained

### 🩺 Tab 1: Prediction
- Enter all 13 health parameters
- Save as patient profile
- Get instant risk assessment
- Download PDF report or CSV

### 📊 Tab 2: Dashboard
- View all predictions
- See statistics (high/low risk cases)
- Export full history

### 📝 Tab 3: Notes & Goals
- Store doctor's notes
- Add and track health goals
- Manage patient information

### ❓ Tab 4: Health Tips
- Heart disease risk factors
- Prevention tips
- BMI calculator
- Lifestyle assessment

### ⚙️ Tab 5: Analytics
- Prediction statistics
- Model performance metrics
- Historical trends

---

## 🌙 Theme Toggle

Click "🌙 Dark Mode" / "☀️ Light Mode" in the sidebar to switch themes.

---

## 💾 Exporting Data

**After Each Prediction:**
- 📥 **CSV**: Single prediction as CSV
- 📄 **PDF**: Professional report with recommendations
- 📊 **History**: All predictions as CSV (Dashboard tab)

---

## 📈 Understanding Results

### Risk Levels
- 🔴 **CRITICAL** (>80% probability) - Seek immediate care
- 🟠 **HIGH** (60-80%) - Consult cardiologist soon
- 🟡 **MODERATE** (40-60%) - Monitor and maintain healthy lifestyle
- 🟢 **LOW** (<40%) - Continue preventive measures

### Health Score
- **0-30**: High Risk
- **30-60**: Moderate Risk
- **60-100**: Low Risk

---

## 🔐 Default Credentials

| Role | Username | Password |
|------|----------|----------|
| Doctor | `doctor` | `doctor123` |
| Patient | `patient` | `patient123` |
| Admin | `admin` | `admin123` |

⚠️ **Change these before production deployment!**

---

## 🐳 Docker Quick Start

```bash
# Start with Docker Compose
docker-compose up -d

# Access at http://localhost:8501
```

---

## 🧪 Run Tests

```bash
pytest test_model.py -v
```

---

## 📚 Documentation

- **Full Guide**: See README.md
- **Deployment**: See DEPLOYMENT_GUIDE.md
- **All Changes**: See ENHANCEMENTS_SUMMARY.md

---

## ❓ FAQ

**Q: Where are predictions logged?**
A: In `prediction_logs/` folder as JSON and CSV files

**Q: How do I change the theme colors?**
A: Edit `.streamlit/config.toml` or `app_enhanced.py`

**Q: Can I use this for real diagnosis?**
A: No! Always consult a healthcare professional. This is for research only.

**Q: How accurate is the model?**
A: 88.33% accuracy on test set (297 samples)

**Q: Can I add more users?**
A: Yes, edit `credentials.yaml` and add new credentials

---

## 📞 Support

- Check README.md for detailed documentation
- See DEPLOYMENT_GUIDE.md for deployment help
- Read ENHANCEMENTS_SUMMARY.md for feature details

---

## 🎓 Learning Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [Random Forest](https://scikit-learn.org/stable/modules/ensemble.html#forests)
- [Heart Disease Risk Factors](https://www.cdc.gov/heartdisease/risk_factors.htm)

---

**Version**: 2.0 (With All Enhancements)
**Status**: Production Ready ✅
**Last Updated**: 2024-01-28
