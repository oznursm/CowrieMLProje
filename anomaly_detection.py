import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("features.csv")

features = [
    'username_enc', 'password_enc', 'src_ip_enc', 'eventid_enc',
    'hour', 'src_ip_attempts', 'password_attempts'
]
X = df[features]

model = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = model.fit_predict(X)  # -1: anomali, 1: normal

df.to_csv("anomaly_results.csv", index=False)
print(df[df['anomaly'] == -1])