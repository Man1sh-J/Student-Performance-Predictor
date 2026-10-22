
import streamlit as st
import pandas as pd
import joblib

# Load our trained AI model
model = joblib.load("student_model.pkl")

# Website heading
st.title("Student Performance Predictor")

st.write("Predict student marks using Machine Learning")
st.info("This is an educational AI/ML project.")

# Get student information
study_hours = st.slider(
    "Study Hours Per Day", 1.0, 10.0, 5.0
)

attendance = st.slider(
    "Attendance Percentage", 50, 100, 80
)

previous_marks = st.slider(
    "Previous Exam Marks", 30, 95, 70
)

# Predict marks
if st.button("Predict Marks"):

    student = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance],
        "Previous_Marks": [previous_marks]
    })

    prediction = model.predict(student)[0]

    # Keep displayed marks between 0 and 100
    prediction = max(0, min(100, prediction))

    st.success(
        f"Predicted Final Marks: {prediction:.2f}/100"
    )

    st.caption(
        "Demo prediction based on synthetic training data. "
        "Not validated for real student performance."
    )
