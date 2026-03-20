import pandas as pd
import folium
from folium.plugins import HeatMap

# Load data
df = pd.read_csv('seattle_areas.csv')

# Create base map
seattle_map = folium.Map(
    location=[47.6062, -122.3321],
    zoom_start=11
)

# Add heatmap
heat_data = [[row['latitudes'], row['longitudes'], row['underserved_probability']] 
             for idx, row in df.iterrows()]

HeatMap(heat_data, 
        min_opacity=0.3,
        radius=25,
        blur=30,
        gradient={0.0: 'green', 0.5: 'yellow', 1.0: 'red'}
).add_to(seattle_map)

light_rail = [
    [47.5, -122.33],
    [47.55, -122.33],
    [47.6, -122.33],
    [47.65, -122.33],
    [47.7, -122.33]
]

subway = [
    [47.6, -122.33],
    [47.6, -122.23],
    [47.6, -121.0]
        ]

folium.PolyLine(
    light_rail,
    color='blue',
    weight=4,
    opacity=0.8,
    popup='Light Rail'
).add_to(seattle_map)

folium.PolyLine(
    subway,
    color='green',
    weight=4,
    opacity=0.8,
    popup='Subway'
).add_to(seattle_map)


seattle_map.save('seattle_complete_map.html')
print("Complete map with transit lines saved!")
