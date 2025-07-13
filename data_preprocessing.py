import pandas as pd

df = pd.read_csv("cowrie_logs.csv", header=0)

# Gerekli sütunları seç
df = df[['timestamp', 'username', 'password', 'src_ip', 'eventid']]

# Doğru formatı belirt!
df['timestamp'] = pd.to_datetime(
    df['timestamp'],
    format='%b %d, %Y @ %H:%M:%S.%f',
    errors='coerce'
)

# Eksik satırları sil
df = df.dropna()

print(df.info())
print(df.head())

df.to_csv("preprocessed.csv", index=False)