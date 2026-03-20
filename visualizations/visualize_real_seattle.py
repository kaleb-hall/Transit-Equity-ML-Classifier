import pandas as pd
import folium
from folium.plugins import HeatMap

# Load the processed data
df = pd.read_csv('seattle_real_processed.csv')

# Create map centered on Seattle
seattle_map = folium.Map(
    location=[47.6062, -122.3321],
    zoom_start=11
)

# Add heatmap
heat_data = [[row['latitude'], row['longitude'], row['underserved_probability']] 
             for idx, row in df.iterrows()]

HeatMap(heat_data,
        min_opacity=0.4,
        radius=20,
        blur=25,
        gradient={0.0: 'green', 0.5: 'yellow', 1.0: 'red'}
).add_to(seattle_map)

# Add markers for the most underserved areas
top_underserved = df.nlargest(10, 'underserved_probability')

for idx, row in top_underserved.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=8,
        color='darkred',
        fill=True,
        popup=f"{row['NAME']}<br>Transit: {row['transit_stops']}<br>Prob: {row['underserved_probability']:.2%}"
    ).add_to(seattle_map)

seattle_map.save('seattle_real_map.html')
print("Real Seattle map saved! Open seattle_real_map.html")
