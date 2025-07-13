import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("anomaly_results.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

plt.figure(figsize=(14, 6))
plt.scatter(df['timestamp'], df['anomaly'], c=df['anomaly'], cmap='coolwarm')
plt.xlabel('Zaman')
plt.ylabel('Anomali (-1: Anomali, 1: Normal)')
plt.title('Cowrie SSH Denemelerinde Anomali Tespiti')

# X ekseninde 2 saatte bir tarih/saat etiketi göster
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=5))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("anomaly_plot.png")