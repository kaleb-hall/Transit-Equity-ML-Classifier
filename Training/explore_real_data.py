import geopandas as gpd

# Load the GeoJSON files (use the uploaded paths)
census = gpd.read_file('/Users/kalebhall/Downloads/2020_Census_Tracts_Seattle_-4161284855353315838.geojson')
transit = gpd.read_file('/Users/kalebhall/Downloads/Seattle_Transportation_Plan_Transit_Element_5878402913453588724.geojson')

print("=== CENSUS TRACTS ===")
print(f"Rows: {len(census)}")
print(f"Columns: {census.columns.tolist()}")
print(census.head())

print("\n" + "="*50 + "\n")

print("=== TRANSIT DATA ===")
print(f"Rows: {len(transit)}")
print(f"Columns: {transit.columns.tolist()}")
print(transit.head())
