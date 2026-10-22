
from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the trained machine learning model
model_path = os.path.join(
    os.path.dirname(__file__),
    "student_model.pkl"
)
model = joblib.load(model_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        study_hours = float(data["study_hours"])
        attendance = float(data["attendance"])
        previous_marks = float(data["previous_marks"])

        # Validate the inputs
        if not (1 <= study_hours <= 10):
            return jsonify({"error": "Study hours must be between 1 and 10"}), 400

        if not (50 <= attendance <= 100):
            return jsonify({"error": "Attendance must be between 50 and 100"}), 400

        if not (30 <= previous_marks <= 95):
            return jsonify({"error": "Previous marks must be between 30 and 95"}), 400

        student = pd.DataFrame({
            "Study_Hours": [study_hours],
            "Attendance": [attendance],
            "Previous_Marks": [previous_marks]
        })

        prediction = float(model.predict(student)[0])
        prediction = max(0, min(100, prediction))

        return jsonify({
            "predicted_marks": round(prediction, 2)
        })

    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid student details"}), 400

if __name__ == "__main__":
    app.run(debug=True)
