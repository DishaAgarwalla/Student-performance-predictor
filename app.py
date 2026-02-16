from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# 🔥 Replace this with your real accuracy from training
MODEL_ACCURACY = 0.91   # Example: if model.score() gave 0.91


@app.route('/')
def home():
    return render_template(
        'index.html',
        accuracy=round(MODEL_ACCURACY * 100, 2)
    )


@app.route('/predict', methods=['POST'])
def predict():
    try:
        study_hours = float(request.form['study_hours'])
        attendance = float(request.form['attendance'])
        previous_marks = float(request.form['previous_marks'])

        # ✅ Validation Rules

        # Study Hours: 0 to 24
        if study_hours < 0 or study_hours > 24:
            raise ValueError("Study hours must be between 0 and 24.")

        # Attendance: 0 to 100
        if attendance < 0 or attendance > 100:
            raise ValueError("Attendance must be between 0 and 100.")

        # Previous Marks: 0 to 100
        if previous_marks < 0 or previous_marks > 100:
            raise ValueError("Previous marks must be between 0 and 100.")

        # 🎯 Make Prediction
        prediction = model.predict([[study_hours, attendance, previous_marks]])
        raw_output = round(prediction[0], 2)

        # 🔒 Cap score between 0 and 100
        if raw_output < 0:
            output = 0
        elif raw_output > 100:
            output = 100
        else:
            output = raw_output

        return render_template(
            'index.html',
            accuracy=round(MODEL_ACCURACY * 100, 2),
            prediction_text=f"Predicted Final Score: {output}",
            study_hours=study_hours,
            attendance=attendance,
            previous_marks=previous_marks
        )

    except ValueError as e:
        return render_template(
            'index.html',
            accuracy=round(MODEL_ACCURACY * 100, 2),
            error_text=str(e),
            study_hours=request.form['study_hours'],
            attendance=request.form['attendance'],
            previous_marks=request.form['previous_marks']
        )


if __name__ == "__main__":
    app.run(debug=True)
