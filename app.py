import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("student_performance_model.pkl")


# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📊",
    layout="centered"
)


# Title
st.title("Student Performance Predictor")

st.write(
    "Enter the student's details below to predict the expected exam score."
)


# Input fields
hours_studied = st.number_input(
    "Hours Studied",
    min_value=1,
    max_value=44,
    value=20
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=60,
    max_value=100,
    value=80
)

parental_involvement = st.selectbox(
    "Parental Involvement",
    ["Low", "Medium", "High"]
)

access_to_resources = st.selectbox(
    "Access to Resources",
    ["Low", "Medium", "High"]
)

extracurricular_activities = st.selectbox(
    "Extracurricular Activities",
    ["No", "Yes"]
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=4,
    max_value=10,
    value=7
)

previous_scores = st.number_input(
    "Previous Scores",
    min_value=50,
    max_value=100,
    value=75
)

motivation_level = st.selectbox(
    "Motivation Level",
    ["Low", "Medium", "High"]
)

internet_access = st.selectbox(
    "Internet Access",
    ["No", "Yes"]
)

tutoring_sessions = st.number_input(
    "Tutoring Sessions",
    min_value=0,
    max_value=8,
    value=1
)

family_income = st.selectbox(
    "Family Income",
    ["Low", "Medium", "High"]
)

teacher_quality = st.selectbox(
    "Teacher Quality",
    ["Low", "Medium", "High"]
)

school_type = st.selectbox(
    "School Type",
    ["Public", "Private"]
)

peer_influence = st.selectbox(
    "Peer Influence",
    ["Negative", "Neutral", "Positive"]
)

physical_activity = st.number_input(
    "Physical Activity (hours)",
    min_value=0,
    max_value=6,
    value=3
)

learning_disabilities = st.selectbox(
    "Learning Disabilities",
    ["No", "Yes"]
)

parental_education_level = st.selectbox(
    "Parental Education Level",
    ["High School", "College", "Postgraduate"]
)

distance_from_home = st.selectbox(
    "Distance from Home",
    ["Near", "Moderate", "Far"]
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)


# Prediction
if st.button("Predict Exam Score"):

    input_data = pd.DataFrame({
        "Hours_Studied": [hours_studied],
        "Attendance": [attendance],
        "Parental_Involvement": [parental_involvement],
        "Access_to_Resources": [access_to_resources],
        "Extracurricular_Activities": [extracurricular_activities],
        "Sleep_Hours": [sleep_hours],
        "Previous_Scores": [previous_scores],
        "Motivation_Level": [motivation_level],
        "Internet_Access": [internet_access],
        "Tutoring_Sessions": [tutoring_sessions],
        "Family_Income": [family_income],
        "Teacher_Quality": [teacher_quality],
        "School_Type": [school_type],
        "Peer_Influence": [peer_influence],
        "Physical_Activity": [physical_activity],
        "Learning_Disabilities": [learning_disabilities],
        "Parental_Education_Level": [parental_education_level],
        "Distance_from_Home": [distance_from_home],
        "Gender": [gender]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Exam Score: {prediction:.2f}")