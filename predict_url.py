import pandas as pd
import joblib

# Load saved model and columns
model = joblib.load("phishing_model.pkl")
columns = joblib.load("model_columns.pkl")

def predict(features_dict):
    # Convert dict → DataFrame
    X = pd.DataFrame([features_dict], columns=columns)
    prediction = model.predict(X)[0]

    # Map result
    if prediction == -1:
        return "🔴 Phishing site"
    elif prediction == 0:
        return "🟡 Suspicious / Unclear"
    else:
        return "🟢 Legitimate site"

# Example test
if __name__ == "__main__":
    sample = {
        "SFH": 1,
        "popUpWindow": -1,
        "SSLfinal_State": 1,
        "Request_URL": -1,
        "URL_of_Anchor": 0,
        "web_traffic": 1,
        "URL_Length": 1,
        "age_of_domain": 1,
        "having_IP_Address": 0
    }

    result = predict(sample)
    print("Prediction:", result)
