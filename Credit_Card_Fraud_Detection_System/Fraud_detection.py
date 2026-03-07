import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler
data = pd.read_csv("creditcard.csv")
X = data.drop("Class", axis=1)
y = data["Class"]
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print("Training Logistic Regression...")
lr_model = LogisticRegression(max_iter=2000, solver="liblinear", random_state=42)
print("Training Random Forest...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
lr_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)
models = {
    "Logistic Regression": lr_model,
    "Random Forest": rf_model
}
for name, model in models.items():
    predictions = model.predict(X_test)
    print(f"\nSample predictions for {name}:")
    for i in range(10):
        if predictions[i] == 1:
            label = "Fraud"
        else:
            label = "Legitimate"
        print(f"Transaction {i+1}: {label}")
    precision = precision_score(y_test, predictions)
    recall = recall_score(y_test, predictions)
    f1 = f1_score(y_test, predictions)
    print(f"\nModel: {name}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}") 



#OUTPUT:
#Training Logistic Regression...
#Training Random Forest...

#Sample predictions for Logistic Regression:
#Transaction 1: Legitimate
#Transaction 2: Legitimate
#Transaction 3: Legitimate
#Transaction 4: Legitimate
#Transaction 5: Legitimate
#Transaction 6: Legitimate
#Transaction 7: Legitimate
#Transaction 8: Legitimate
#Transaction 9: Legitimate
#Transaction 10: Legitimate

#Model: Logistic Regression
#Precision: 0.8289
#Recall: 0.6429
#F1 Score: 0.7241

#Sample predictions for Random Forest:
#Transaction 1: Legitimate
#Transaction 2: Legitimate
#Transaction 3: Legitimate
#Transaction 4: Legitimate
#Transaction 5: Legitimate
#Transaction 6: Legitimate
#Transaction 7: Legitimate
#Transaction 8: Legitimate
#Transaction 9: Legitimate
#Transaction 10: Legitimate

#Model: Random Forest
#Precision: 0.9412
#Recall: 0.8163
#F1 Score: 0.8743
