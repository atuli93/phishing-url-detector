# 🛡️ Phishing URL Detector

A machine learning project that detects whether a URL is **legitimate** or **phishing**.  
Built with **Python, Flask, and Scikit-learn**.

---

## 🚀 Features
- Train a model on phishing datasets
- Predict if a given URL is safe or suspicious
- Simple Flask web app with user-friendly input form
- Ready for deployment

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/atuli93/phishing-url-detector.git
   cd phishing-url-detector
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the Flask app:
```bash
python app.py
```

Visit in your browser:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📂 Project Structure
```
phishing-url-detector/
│── app.py                # Flask app
│── train_model.py        # Train the ML model
│── predict_url.py        # Prediction script
│── save_model.py         # Save trained model
│── test_dataset.py       # Test dataset handling
│── templates/index.html  # Web UI
│── data/phishing.csv     # Dataset
│── requirements.txt      # Dependencies
│── README.md             # Project docs
```

---

## 📊 Dataset
This project uses the [UCI Phishing Websites Dataset](https://archive.ics.uci.edu/ml/datasets/phishing+websites).

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

---

## 📜 License
MIT License © 2025 [atuli93](https://github.com/atuli93)
