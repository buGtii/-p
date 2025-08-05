import arff
import pandas as pd

arff_file = 'Training Dataset.arff'  # Make sure this file is in same folder
with open(arff_file, 'r') as f:
    dataset = arff.load(f)

data = pd.DataFrame(dataset['data'])
columns = [attr[0] for attr in dataset['attributes']]
data.columns = columns

# Save CSV
data.to_csv('phishing_data.csv', index=False)
print("✅ CSV saved as phishing_data.csv")
