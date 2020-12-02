import csv
import json
import difflib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np 

def make_plot(src, dest, path):
	with open('{}states_india.geojson'.format(path), 'r') as file:
		states_geojson = json.load(file)

	geojson_state_code_map = {}
	for feature in states_geojson["features"]:
		feature['id'] = feature['properties']['state_code']
		geojson_state_code_map[feature['properties']['st_nm'].upper()] = feature['properties']['state_code']

	state_id_map = {}
	with open(src, 'r', newline='') as file:
		for row in csv.DictReader(file):
			state = row["State"]
			if state == "DELHI":
				state_id_map[state] = geojson_state_code_map["NCT OF DELHI"]
			else:
				state_id_map[state] = geojson_state_code_map[difflib.get_close_matches(state, geojson_state_code_map.keys())[0]]

	df = pd.read_csv(src)
	df['Frequency'] = df['Frequency'].apply(lambda x: int(x))
	df['id'] = df['State'].apply(lambda x: state_id_map.get(x, 0))


	fig = px.choropleth(df, locations='id', geojson=states_geojson, color='Frequency', scope='asia')
	fig.update_geos(fitbounds="locations", visible=False)
	fig.write_image(dest)