from ucimlrepo import fetch_ucirepo
import pandas as pd
import os

# Make sure "data" folder exists
os.makedirs("data", exist_ok=True)

# Fetch dataset (UCI Website Phishing, ID=379)
data = fetch_ucirepo(id=379)

# Features (X) and target (y)
X = data.data.features
y = data.data.targets

# Rename target column to "Result" if not already
if y.shape[1] == 1:
    y.columns = ["Result"]

# Merge features + target
df = pd.concat([X, y], axis=1)

# Save as CSV
df.to_csv("data/phishing.csv", index=False)

print("✅ Saved CSV with shape:", df.shape)
print("📝 Columns:", df.columns.tolist())

