import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/fires_france.csv")

df["acq_date"] = pd.to_datetime(df["acq_date"])

fires_per_day = df.groupby("acq_date").size()

plt.figure(figsize=(12,6))
fires_per_day.plot()

plt.title("Nombre de feux détectés par jour en France")
plt.xlabel("Date")
plt.ylabel("Nombre de détections")

plt.tight_layout()

plt.savefig("outputs/fires_per_day.png")

daynight_counts = df["daynight"].value_counts()

plt.figure(figsize=(6,6))
daynight_counts.plot(kind="bar")

plt.title("Répartition des détections Jour / Nuit")
plt.xlabel("Période")
plt.ylabel("Nombre de détections")

plt.tight_layout()
plt.savefig("outputs/daynight_distribution.png")

top_days = df.groupby("acq_date").size().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_days.sort_values().plot(kind="barh")

plt.title("Top 10 des journées avec le plus de détections")
plt.xlabel("Nombre de détections")
plt.ylabel("Date")

plt.tight_layout()
plt.savefig("outputs/top10_days.png")

plt.figure(figsize=(8,10))

plt.scatter(
    df["longitude"],
    df["latitude"],
    s=5,
    alpha=0.5,
    color="red"
)

plt.title("Localisation des détections de feux en France")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()
plt.savefig("outputs/fire_locations.png")


plt.show()