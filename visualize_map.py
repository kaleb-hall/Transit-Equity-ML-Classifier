import pandas as pd
import folium

df = pd.read_csv('seattle_areas.csv')

seattle_map = folium.Map(
    location=[47.6062, -122.3321],  # Seattle center
    zoom_start=11
)

for idx, row in df.iterrows():

    c = 'red' if row['underserved'] == 1 else 'green'
    folium.CircleMarker(location=[row['latitudes'], row['longitudes']], radius=5, color=c, fill=True, fillColor=c, fillOpacity=0.6, popup=f"Prob: {row['underserved_probability']:.2f}").add_to(seattle_map)
seattle_map.save('seattle_transit_map.html')
print("Map saved as 'seattle_transit_map.html' - open it in your browser")


