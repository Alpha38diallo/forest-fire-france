import pandas as pd
import folium

df = pd.read_csv("data/fires_france.csv")
m = folium.Map(
    location=[46.6, 2.2],
    zoom_start=6,
    tiles="CartoDB dark_matter"
)

for _, row in df.sample(min(1000, len(df))).iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=2,
        color="red",
        fill=True
    ).add_to(m)

m.save("outputs/fire_map_france.html")

print("Carte créée : outputs/fire_map_france.html")