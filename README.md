Credit Risk Analysis

Overview
This project focuses on building a machine learning pipeline to predict credit risk using a dataset of financial and demographic information. The goal is to classify customers into "good" or "bad" credit risk categories, enabling financial institutions to make informed lending decisions.

The project includes:

Data preprocessing and feature engineering.
Handling imbalanced datasets using techniques like SMOTE.
Training and evaluating multiple machine learning models (e.g., SVM, Gradient Boosting, XGBoost).
Model explainability using SHAP (SHapley Additive exPlanations).

Project Structure
credit_risk/
│
├── data/                     # Raw and processed data files
│
├── notebooks/                # Jupyter notebooks for analysis
│   └── data_exploration.ipynb
|   └── preprocessing_test.ipynb
|   └── main_executor.ipynb
|   └── model_exploration.ipynb
|
├── utils/                    # All required utils and process specific utils files
|   ......
|
├── pipeline/                 # Process specific pipeline and executors
|   ......
│
├── config.yaml               # Configuration file for preprocessing and feature engineering
│
└── README.md                 # Project documentation

Dataset
The dataset used in this project is the German Credit Dataset, which contains the following:

Features: Financial and demographic attributes such as age, credit amount, duration, job, housing, and savings accounts.
Target Variable: Risk (binary classification: "good" or "bad").

Key Steps
1. Data Preprocessing (main_executor.ipnyb)
  Handled missing values by filling with "Unknown" for categorical features like Saving accounts and Checking account.
  Scaled numerical features (Age, Credit amount, Duration) using standard scaling.
2. Feature Engineering (main_executor.ipnyb)
  Applied one-hot encoding to categorical features (Job, Housing, Saving accounts, Checking account, Purpose, Sex).
3. Handling Imbalanced Data (model_exploration.ipynb)
  Used SMOTE (Synthetic Minority Oversampling Technique) to balance the dataset by oversampling the minority class.
4. Model Training (model_exploration.ipynb)
  Trained multiple classification models:
  Support Vector Machine (SVM)
  Gradient Boosting
  XGBoost
  Performed hyperparameter tuning using GridSearchCV.
5. Model Evaluation (model_exploration.ipynb)
  Evaluated models using metrics such as:
  Accuracy
  Precision
  Recall
  F1 Score
  ROC AUC
  PR AUC

Results: 
Models created with balanced and imbalanced dataset (model_exploration.ipynb)
