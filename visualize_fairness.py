import pandas as pd
import folium
import geopandas as gpd


df = pd.read_csv('seattle_with_demographics.csv')

# Create two maps side-by-side view
seattle_map = folium.Map(
    location=[47.6062, -122.3321],
    zoom_start=11
)
transit = gpd.read_file('/Users/kalebhall/Downloads/Seattle_Transportation_Plan_Transit_Element_5878402913453588724.geojson')
transit_latlon = transit.to_crs(epsg=4326)

for idx, row in transit_latlon.iterrows():
    # Determine color based on transit type
    ftv_type = str(row.get('FTV_pdt', '')).lower()
    rapid_ride = str(row.get('RapidRd', '')).lower()
    future_link = row.get('ftrLINK', 0)
    
    # Color coding
    if future_link > 0 or 'link' in ftv_type:
        color = 'blue'  # Light rail
        weight = 4
        label = 'Light Rail'
    elif 'rapid' in rapid_ride or 'rapid' in ftv_type:
        color = 'red'  # RapidRide (BRT)
        weight = 4
        label = 'RapidRide'
    else:
        color = 'orange'  # Regular buses
        weight = 4
        label = 'Bus'
    
    # Handle both single and multi-part geometries
    geom = row.geometry
    if geom.geom_type == 'LineString':
        coords = [(point[1], point[0]) for point in geom.coords]
        folium.PolyLine(coords, color=color, weight=weight, opacity=0.7,
                       popup=f"{label}<br>Route: {row.get('routes', 'N/A')}").add_to(seattle_map)
    elif geom.geom_type == 'MultiLineString':
        for line in geom.geoms:
            coords = [(point[1], point[0]) for point in line.coords]
            folium.PolyLine(coords, color=color, weight=weight, opacity=0.7,
                           popup=f"{label}<br>Route: {row.get('routes', 'N/A')}").add_to(seattle_map)

for idx, row in df.iterrows():
    # Color logic:
    # Red circle = Minority + Underserved
    # Orange circle = White + Underserved  
    # Blue circle = Minority + Not underserved
    # Green circle = White + Not underserved
    
    if row['majority_minority'] == 1 and row['underserved'] == 1:
        color = 'red'
        label = "Minority + Underserved"
    elif row['majority_minority'] == 0 and row['underserved'] == 1:
        color = 'orange'
        label = "White + Underserved"
    elif row['majority_minority'] == 1:
        color = 'blue'
        label = "Minority + Served"
    else:
        color = 'green'
        label = "White + Served"
    
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        color=color,
        fill=True,
        fillColor=color,
        fillOpacity=0.6,
        popup=f"{row['NAME']}<br>{label}<br>Transit: {row['transit_stops']}<br>Prob: {row['underserved_probability']:.2%}"
    ).add_to(seattle_map)

seattle_map.save('seattle_fairness_map.html')
print("Fairness map saved!")
print("\nLegend:")
print("Red = Majority-minority + Underserved")
print("Orange = Majority-white + Underserved")
print("Blue = Majority-minority + Served")
print("Green = Majority-white + Served")
