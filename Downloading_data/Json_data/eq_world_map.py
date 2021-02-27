import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline  # render the map

# Explore the structure of the data
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))    # 158

# extracting magnitudes, longitudes, latitudes
mags, lons, lats, hover_texts = [], [], [], []   # magnitude
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']      # title will be hover_texts
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# print(mags[:10])    # first 10 magnitudes: [0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
# print(lons[:5])     # first 5 longitudes: [-116.7941667, -148.9865, -74.2343, -161.6801, -118.5316667]
# print(lats[:5])     # first 5 latitudes: [33.4863333, 64.6673, -12.1025, 54.2232, 35.3098333]

# Map the earthquakes
# list of data; Scattergeo allow overlay a scatter plot of geographic data
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],    # marker size
        'color': mags,                      # mags list to determine the color
        'colorscale': 'Viridis',            # color range from dark blue to bright yellow
        'reversescale': True,               # bright yellow: lowest value; dark blue: most severe earthquakes
        'colorbar': {'title': 'Magnitude'}, # colorscale of colorbar
    },
}]

my_layout = Layout(title='Global Earthquakes')  # set chart title

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')   # display output on a html file
