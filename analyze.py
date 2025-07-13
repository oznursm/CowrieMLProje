import pandas as pd

# CSV'yi yükle
df = pd.read_csv("cowrie_logs.csv", header=0)

print(df.head())  # İlk 5 satırı yazdır