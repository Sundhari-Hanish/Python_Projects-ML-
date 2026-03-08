import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings("ignore")
data = pd.read_csv("train_u6lujuX_CVtuZ9i.csv")
data = data.drop("Loan_ID", axis=1)
data["LoanAmount"] = data["LoanAmount"].fillna(data["LoanAmount"].median())
data["Loan_Amount_Term"] = data["Loan_Amount_Term"].fillna(data["Loan_Amount_Term"].median())
data["Credit_History"] = data["Credit_History"].fillna(data["Credit_History"].median())
data["Gender"] = data["Gender"].fillna(data["Gender"].mode()[0])
data["Married"] = data["Married"].fillna(data["Married"].mode()[0])
data["Dependents"] = data["Dependents"].fillna(data["Dependents"].mode()[0])
data["Self_Employed"] = data["Self_Employed"].fillna(data["Self_Employed"].mode()[0])
label_encoder = LabelEncoder()
categorical_columns = data.select_dtypes(include=["object"]).columns
for col in categorical_columns:
    data[col] = label_encoder.fit_transform(data[col])
X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
print("Model Training Completed")
y_pred = model.predict(X_test)
print("\nEnter Applicant Details")
gender = int(input("Gender (1=Male, 0=Female): "))
married = int(input("Married (1=Yes, 0=No): "))
dependents = int(input("Dependents (0,1,2,3): "))
education = int(input("Education (1=Graduate, 0=Not Graduate): "))
self_employed = int(input("Self Employed (1=Yes, 0=No): "))
applicant_income = int(input("Applicant Income: "))
coapplicant_income = int(input("Coapplicant Income: "))
loan_amount = int(input("Loan Amount: "))
loan_term = int(input("Loan Amount Term: "))
credit_history = int(input("Credit History (1=Good, 0=Bad): "))
property_area = int(input("Property Area (0=Rural,1=Semiurban,2=Urban): "))
user_data = np.array([[gender, married, dependents, education, self_employed,
                       applicant_income, coapplicant_income,
                       loan_amount, loan_term, credit_history, property_area]])
result = model.predict(user_data)
print("\nLoan Approval Result:")
if result[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")
