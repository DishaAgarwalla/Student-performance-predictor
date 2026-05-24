# 🎓 Student Performance Prediction System

<p align="center">
  <a href="http://student-performance-predictor-2oxh.onrender.com/" target="_blank">
    <img src="https://img.shields.io/badge/🎓%20Live%20Demo-Student%20Performance%20Predictor-blue?style=for-the-badge">
  </a>
</p>

A Machine Learning web application that predicts a student's final exam score based on:

- 📚 Study Hours
- 🏫 Attendance Percentage
- 📝 Previous Marks

The system compares multiple ML models and automatically selects the best performing model.

---

## 🚀 Features

✅ Input Validation (Frontend + Backend)  
✅ Model Comparison (Linear Regression vs Random Forest)  
✅ Automatic Best Model Selection  
✅ Accuracy Display  
✅ Score Capped Between 0–100  
✅ Clean Flask Web Interface  

---

## 🧠 Machine Learning Details

### Models Used:
- Linear Regression
- Random Forest Regressor

### Model Comparison Results:

| Model | Accuracy (R² Score) |
|-------|----------------------|
| Linear Regression | **93.17%** |
| Random Forest | 83.98% |

🏆 **Best Model Selected: Linear Regression**

---

## 📊 Dataset

The dataset includes 150 realistic samples with the following features:

- Study Hours (0–24)
- Attendance (40–100)
- Previous Marks (40–100)
- Final Score (0–100)

The data is generated with realistic noise to simulate real-world patterns.

---

## 🖥️ Technologies Used

- Python
- Flask
- Scikit-Learn
- Pandas
- HTML/CSS

---

## ⚙️ How to Run This Project

1️⃣ Clone the repository:

```bash
git clone https://github.com/DishaAgarwalla/Student-performance-predictor.git
```

2️⃣ Navigate to the project folder:

```bash
cd Student-performance-predictor
```

3️⃣ Create virtual environment:

```bash
python -m venv venv
```

4️⃣ Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

5️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

6️⃣ Run the Flask app:

```bash
python app.py
```

7️⃣ Open in browser:

```bash
http://127.0.0.1:5000
```

---

## 👩‍💻 Author

**Disha Agarwalla**
