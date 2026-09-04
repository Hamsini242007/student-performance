# Student Performance Predictor

A Machine Learning application that predicts a student's expected exam score based on academic, personal, and environmental factors.

## Project Overview

This project uses Machine Learning to predict student exam performance based on factors such as:

- Hours Studied
- Attendance
- Parental Involvement
- Access to Resources
- Extracurricular Activities
- Sleep Hours
- Previous Scores
- Motivation Level
- Internet Access
- Tutoring Sessions
- Family Income
- Teacher Quality
- School Type
- Peer Influence
- Physical Activity
- Learning Disabilities
- Parental Education Level
- Distance from Home
- Gender

The project demonstrates a complete Machine Learning workflow, including data preprocessing, model training, evaluation, feature engineering experiments, model comparison, and a Streamlit application for predictions.

## Dataset

The dataset contains student performance information with **6,607 records and 20 columns**.

The target variable is:

`Exam_Score`

During data cleaning, one record with an exam score greater than 100 was removed. The final dataset used for model training contained **6,606 records**.

## Data Preprocessing

The following steps were performed:

- Checked the dataset shape and data types
- Checked for missing values
- Checked for duplicate rows
- Removed one invalid exam score greater than 100
- Handled missing categorical values using the most frequent value
- Encoded categorical variables using One-Hot Encoding
- Split the dataset into training and testing sets

## Models Used

Two regression models were trained and compared:

1. Linear Regression
2. Random Forest Regressor

A feature engineering experiment was also performed by creating the following interaction features:

- `Study_Attendance`
- `Previous_Attendance`

## Model Performance

| Model | MAE | MSE | RMSE | R² Score |
|---|---:|---:|---:|---:|
| Linear Regression | **0.416** | **2.314** | 1.521 | 0.825 |
| Random Forest | 1.071 | 3.927 | 1.982 | 0.703 |
| Feature Engineered Linear Regression | 0.420 | **2.312** | **1.521** | **0.825** |
| Feature Engineered Random Forest | 1.034 | 3.808 | 1.951 | 0.712 |

Linear Regression was selected as the final model because it achieved the best overall performance while remaining simpler than the other models.

## Evaluation Metrics

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## Streamlit Application

The Streamlit application allows users to enter student-related information and receive a predicted exam score.

Run the application locally using:

```bash
streamlit run app.py
```

## Project Structure

```text
ml/
│
├── StudentPerformanceFactors.csv
├── notebook.ipynb
├── student_performance_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Hamsini242007/student-performance.git
```

Navigate to the project directory:

```bash
cd student-performance
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## Future Improvements

- Experiment with additional regression models
- Perform hyperparameter tuning
- Add more visualizations to the Streamlit application
- Deploy the application publicly

## Author

**Hamsini Lalith Karkera**