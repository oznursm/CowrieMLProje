import pandas as pd

df = pd.read_csv("anomaly_results.csv")
df[df['anomaly'] == -1].to_csv("anomalies.csv", index=False)
print("Anomaliler anomalies.csv dosyasına kaydedildi.")