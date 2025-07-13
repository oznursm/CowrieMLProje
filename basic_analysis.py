import pandas as pd

df = pd.read_csv("features.csv")

# En çok denenen şifreler
print("En çok denenen şifreler:")
print(df['password'].value_counts())

# En çok saldırı yapan IP'ler
print("\nEn çok saldırı yapan IP'ler:")
print(df['src_ip'].value_counts())