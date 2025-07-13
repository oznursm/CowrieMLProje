import pandas as pd

df = pd.read_csv("encoded.csv")

# Saat bilgisini çıkart
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour

# Her IP'nin toplam deneme sayısı
df['src_ip_attempts'] = df.groupby('src_ip')['src_ip'].transform('count')

# Her şifrenin toplam deneme sayısı
df['password_attempts'] = df.groupby('password')['password'].transform('count')

df.to_csv("features.csv", index=False)
print(df[['timestamp', 'src_ip', 'password', 'hour', 'src_ip_attempts', 'password_attempts']].head())