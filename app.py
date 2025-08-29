from flask import Flask, render_template, request
import joblib
import numpy as np

# Load trained model
model = joblib.load("phishing_model.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            int(request.form["SFH"]),
            int(request.form["popUpWindow"]),
            int(request.form["SSLfinal_State"]),
            int(request.form["Request_URL"]),
            int(request.form["URL_of_Anchor"]),
            int(request.form["web_traffic"]),
            int(request.form["URL_Length"]),
            int(request.form["age_of_domain"]),
            int(request.form["having_IP_Address"]),
        ]
        prediction = model.predict([features])[0]

        if prediction == 1:
            result = "🟢 Legitimate Website"
        elif prediction == -1:
            result = "🔴 Phishing Website"
        else:
            result = "🟡 Suspicious Website"

    except Exception as e:
        result = f"⚠️ Error: {e}"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
