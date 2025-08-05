import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump

# ✅ Corrected CSV path (Use raw string or double backslash)
df = pd.read_csv(r"C:\Users\Faisal_bugti\Desktop\phishing_url_detecter\phishing_data.csv")

# 👀 Print available columns in CSV
print("Available columns in dataset:\n", df.columns)

# ✅ Use only existing features
# Update this list according to the printed column names
selected_features = [
    'having_IP_Address',
    'URL_Length',
    'having_At_Symbol',
    'double_slash_redirecting',
    'Prefix_Suffix'
    # 'Subdomain' removed since it's missing
]

# Features & Labels
X = df[selected_features]
y = df['Result']

# ✅ Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# ✅ Save Model
dump(model, "phishing_model_light.joblib")
print("✅ Lightweight phishing detection model trained and saved successfully!")
