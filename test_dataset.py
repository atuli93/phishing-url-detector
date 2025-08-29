import pandas as pd

# Load dataset
df = pd.read_csv("data/phishing.csv")

print("✅ Dataset loaded!")
print("Shape:", df.shape)
print("\n🔹 First 5 rows:")
print(df.head())

print("\n🔹 Class distribution (Result column):")
print(df["Result"].value_counts())
