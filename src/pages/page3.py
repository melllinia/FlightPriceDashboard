import pandas as pd
from dash import dcc, html
import plotly.express as px
from src.pages.page1 import city_counts
from data_loader import df


lat_long = {
    'Mumbai': [19.076090, 72.877426],
    'Delhi': [28.679079, 77.069710],
    'Bangalore': [12.971599, 77.5946],
    'Kolkata': [22.5726, 88.3639],
    'Hyderabad': [17.4065, 78.4772],
    'Chennai': [13.0827, 80.2707]
}


def map_lat_long(city):
    return lat_long.get(city)


df[['from_latitude', 'from_longitude']] = df['source_city'].apply(lambda x: pd.Series(map_lat_long(x)))
df[['to_latitude', 'to_longitude']] = df['destination_city'].apply(lambda x: pd.Series(map_lat_long(x)))

# Convert lat_long dictionary to DataFrame for easier manipulation
lat_long_df = pd.DataFrame.from_dict(lat_long, orient='index', columns=['Latitude', 'Longitude'])
lat_long_df['City'] = lat_long_df.index

# Define a scatter mapbox figure using Plotly Express
fig = px.scatter_mapbox(lat_long_df, lat="Latitude", lon="Longitude", hover_name="City",
                        hover_data=["Latitude", "Longitude"],
                        size=city_counts['Total'] / 100,
                        color_discrete_sequence=["#40498e"], zoom=3)

fig.update_layout(mapbox_style="carto-positron")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Define the layout for the third page
layout = html.Div([
    html.H1('Total Number of Arrivals and Departures of The Cities on Map', style={'color': 'navy'}),
    dcc.Graph(figure=fig)  # Display the Plotly figure
])
