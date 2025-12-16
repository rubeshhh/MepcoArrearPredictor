import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def train_model():
    # Sample dataset (realistic values should be used later)
    data = {
        "StudyHours": [2,3,4,5,6,7,8,9],
        "Attendance": [55,60,65,70,75,80,85,90],
        "CGPA": [5.5,6.0,6.2,6.8,7.2,7.8,8.2,8.8],
        "Assignment": [4,5,6,7,8,9,9,10],
        "CTT": [6,7,8,9,10,12,13,14],
        "Internal300": [120,135,150,165,180,195,210,225],
        "PrevArrears": [3,2,2,1,1,0,0,0],
        "Result": [0,0,0,1,1,1,1,1]
    }

    df = pd.DataFrame(data)

    # Features and target
    X = df.drop("Result", axis=1)
    y = df["Result"]

    # Feature scaling to 0-1
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Train Logistic Regression
    model = LogisticRegression()
    model.fit(X_scaled, y)

    return model, scaler

# Train model once
model, scaler = train_model()

def predict_result(
    study_hours,
    attendance,
    cgpa,
    assignment,
    ctt,
    internal_300,
    prev_arrears
):
    # Attendance rule
    if attendance < 75:
        return 0, 0.0

    # Mild cramming penalty
    if study_hours > 4:
        effective_hours = study_hours * 0.85
    else:
        effective_hours = study_hours

    # Prepare features array
    features = np.array([[
        effective_hours,
        attendance,
        cgpa,
        assignment,
        ctt,
        internal_300,
        prev_arrears
    ]])

    # Scale features
    features_scaled = scaler.transform(features)

    # Prediction
    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][1]

    return prediction, round(probability * 100, 2)
