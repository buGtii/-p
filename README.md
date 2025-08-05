# 🔐 Phishing URL Detection (Lightweight Model)

This project implements a lightweight **Phishing URL Detector** using selected basic features extracted from a URL. It predicts whether a given URL is **legitimate** or **phishing** using a trained machine learning model.

---

## 🚀 Features Used

The model uses the following lightweight URL features:

- Whether the URL uses an IP address
- Length of the URL
- Presence of '@' symbol
- Presence of double slashes '//' (redirect)
- Presence of '-' (prefix/suffix) in the domain
- Number of subdomains

---

## 🛠️ Requirements

- Python ≥ 3.7
- Required Python packages:
 
  pip install pandas scikit-learn joblib liac-arff
📦 Installation
Install Python from https://www.python.org/downloads/

Install the required libraries:


pip install pandas scikit-learn joblib liac-arff
📁 Dataset
The original dataset is in .arff format and needs to be converted to .csv before training.

➤ Convert ARFF to CSV
Use the following code to convert the dataset:


from scipy.io import arff
import pandas as pd

data = arff.loadarff('TrainingDataset.arff')
df = pd.DataFrame(data[0])
df.to_csv('TrainingDataset.csv', index=False)
print("Dataset successfully converted to CSV!")
🧠 Model Training
Run the following script to train your model:


python train_model.py
It will create a trained model file named:


phishing_model_light.joblib
🔍 URL Prediction
Once your model is trained, run the following script to check a URL:


python predict_url.py
You will be prompted to enter a URL, and the model will classify it as either:

Legitimate

Phishing

📂 Project Structure

phishing-url-detector/
│
├── TrainingDataset.arff           # Original ARFF dataset
├── TrainingDataset.csv            # Converted CSV dataset
├── train_model.py                 # Training script
├── predict_url.py                 # Prediction script
├── phishing_model_light.joblib    # Trained model file
                    
📌 Notes
This is a basic phishing detector using only 6 features for fast and lightweight detection.

For more accurate results, you can extend the feature set and retrain the model.

This project is meant for educational and learning purposes.

👨‍💻 Author
Muhammad Faisal
📧 Email: faisal.bugti65@gmail.com
🔗 LinkedIn: linkedin.com/in/muhammad-faisal-76a6362b5

✅ License
MIT License - You can freely use, modify, and share this project.

Happy Learning & Stay Secure! 🔐
