import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("preprocessed.csv")

le_user = LabelEncoder()
le_pw = LabelEncoder()
le_ip = LabelEncoder()
le_event = LabelEncoder()

df['username_enc'] = le_user.fit_transform(df['username'])
df['password_enc'] = le_pw.fit_transform(df['password'])
df['src_ip_enc'] = le_ip.fit_transform(df['src_ip'])
df['eventid_enc'] = le_event.fit_transform(df['eventid'])

df.to_csv("encoded.csv", index=False)
print(df.head())