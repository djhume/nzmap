"""
Simple script showing how to bind python data to a topojson in an interactive
map using folium

Author: Nigel Cleland
contact: nigel.cleland@gmail.com
license: MIT
"""

# Initial Preamble
import pandas as pd
import folium

price_data = 'price_test.csv'
nz_json = 'NZ_high_topo.json'

prices = pd.read_csv(price_data)

# Create a Folium Map, location is set to NZ (had to tweak this a bit)
# Note that a lower zoom_start, zooms out the starting point
fmap = folium.Map(location=[-41.5, 174], zoom_start=6, width=700, height=900)

# Bind the TopoJSON and csv price data to an interactive map
# Notes:
#    topojson: must begin with objects.<name>
#    key_on: must begin with feature.<name>
fmap.geo_json(geo_path=nz_json, 
    topojson='objects.NZ_high_gxps_transformed_new',
    key_on='feature.id',
    fill_color='YlGn',
    data=prices,
    columns=['gxp', 'price'],
    threshold_scale=[50,55,60,65,70,80],
    legend_name="Electricity Spot Price [$/MWh]",
    fill_opacity=0.7, line_opacity=0.5)
# Create the map
fmap.create_map(path='folium_test.html')
