import pandas as pd
import folium
from folium.plugins import HeatMap

df = pd.read_csv('seattle_areas.csv')

seattle_map = folium.Map(
    location=[47.6062, -122.3321],  # Seattle center
    zoom_start=11
)

heat_data = [[row['latitudes'], row['longitudes'], row['underserved_probability']] for idx, row in df.iterrows()]

HeatMap(heat_data, min_opacity=0.3, radius=40, blur=50, gradient={0.0: 'green', 0.5: 'yellow', 0.8: 'red'}).add_to(seattle_map)

seattle_map.save('seattle_heatmap.html')
print("Heatmap saved as 'seattle_heatmap.html'!")

