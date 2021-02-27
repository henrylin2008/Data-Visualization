import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline  # render the map

# Explore the structure of the data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))    # 158

# extracting magnitudes, longitudes, latitudes
mags, lons, lats = [], [], []   # magnitude
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])    # first 10 magnitudes: [0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
print(lons[:5])     # first 5 longitudes: [-116.7941667, -148.9865, -74.2343, -161.6801, -118.5316667]
print(lats[:5])     # first 5 latitudes: [33.4863333, 64.6673, -12.1025, 54.2232, 35.3098333]
