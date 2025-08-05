import re
import joblib
import pandas as pd
from urllib.parse import urlparse

# Model load
model = joblib.load("phishing_model_light.joblib")

# ---- Feature extraction ----
def having_ip(url):
    return 1 if re.search(r'(\d{1,3}\.){3}\d{1,3}', url) else -1

def url_length(url):
    return 1 if len(url) < 54 else 0 if len(url) <= 75 else -1

def having_at_symbol(url):
    return 1 if "@" not in url else -1

def double_slash_redirecting(url):
    return -1 if url.count("//") > 1 else 1

def prefix_suffix(url):
    return -1 if "-" in urlparse(url).netloc else 1

def subdomain(url):
    dots = urlparse(url).netloc.split(".")
    return -1 if len(dots) > 3 else 1

def extract_features(url):
    return [
        having_ip(url),
        url_length(url),
        having_at_symbol(url),
        double_slash_redirecting(url),
        prefix_suffix(url),
        subdomain(url)
    ]

# ---- User input ----
url = input("Enter URL to check: ")
features = extract_features(url)

# DataFrame for prediction
df = pd.DataFrame([features], columns=[
    'having_IP_Address',
    'URL_Length',
    'having_At_Symbol',
    'double_slash_redirecting',
    'Prefix_Suffix',
    'Subdomain'
])

prediction = model.predict(df)[0]
print("Prediction:", "Phishing Website" if prediction == -1 else "Legitimate Website")
