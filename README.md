# Student Performance Predictor

A machine learning web application that predicts students' final exam marks based on study hours, attendance percentage, and previous exam marks.

## Live Demo

[Try the Student Performance Predictor](https://student-performance-predictor-two-nu.vercel.app)

## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn (Linear Regression)
- Flask
- HTML, CSS, and JavaScript
- Google Colab
- GitHub
- Vercel

## Features

- Enter daily study hours
- Enter attendance percentage
- Enter previous exam marks
- Predict final exam marks using a trained machine learning model
- Responsive web interface

## Model Performance

The model was trained on a synthetic dataset containing 500 student records.

- Algorithm: Linear Regression
- Training records: 400
- Testing records: 100
- Mean Absolute Error (MAE): approximately 3.9
- R² Score: approximately 0.89

**Important:** These results are based on synthetic data. The model has not been validated on real student records and should be treated as an educational demonstration.

## How It Works

1. The user enters student information through the website.
2. The Flask backend receives the information.
3. The trained machine learning model predicts final marks.
4. The website displays the predicted result.

## Developer

Developed as a beginner AI/ML portfolio project to practice machine learning, Python backend development, and web deployment.
