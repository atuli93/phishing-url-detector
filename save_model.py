import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("data/phishing.csv")
X = df.drop("Result", axis=1)
y = df["Result"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model + columns
joblib.dump(model, "phishing_model.pkl")
joblib.dump(list(X.columns), "model_columns.pkl")

print("✅ Model saved as phishing_model.pkl")
