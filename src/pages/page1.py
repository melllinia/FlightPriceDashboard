from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go

# Load and preprocess the data
df = pd.read_csv('../data/flights_dataset.csv')
df = df.drop(df.columns[0], axis=1)

# Price is in Indian rupees, let us convert it to USD
df['price'] = df['price'].div(83).round(2)

# Pie chart
class_counts = df['class'].value_counts()
colors = ['#332345', '#40498e']
fig_pie = go.Figure(data=[go.Pie(labels=class_counts.index,
                                 values=class_counts.values,
                                 marker=dict(colors=colors),
                                 textinfo='percent',
                                 textposition='inside'
                                )
                         ])
fig_pie.update_layout(
    title="Number of flights in Business vs Economy Class",
    title_font=dict(color='navy')
)

# Stacked bar chart
departure_counts = df['source_city'].value_counts()
arrival_counts = df['destination_city'].value_counts()
city_counts = pd.concat([departure_counts, arrival_counts], axis=1, keys=['Departures', 'Arrivals'])
city_counts['Total'] = city_counts['Departures'] + city_counts['Arrivals']
city_counts.sort_values(by='Total', ascending=False, inplace=True)

trace1 = go.Bar(x=city_counts.index, y=city_counts['Departures'], name='Departures', marker=dict(color='#3e356b'))
trace2 = go.Bar(x=city_counts.index, y=city_counts['Arrivals'], name='Arrivals', marker=dict(color='#357ba3'))
fig_bar = go.Figure(data=[trace1, trace2])
fig_bar.update_layout(barmode='stack',
                      title='Departures and Arrivals by City',
                      xaxis=dict(title='City', tickfont=dict(size=14)),
                      yaxis=dict(title='Flight Count', tickfont=dict(size=14)),
                      legend=dict(font=dict(size=12))
                     )

# Violin plot
fig_violin = go.Figure()
economy_airlines = df[df["class"] == 'Economy']["airline"].unique()
for airline in economy_airlines:
    economy_data = df[(df["class"] == 'Economy') & (df["airline"] == airline)]
    fig_violin.add_trace(go.Violin(y=economy_data["price"], name=f'{airline} - Economy'))

business_airlines = df[df["class"] == 'Business']["airline"].unique()
for airline in business_airlines:
    business_data = df[(df["class"] == 'Business') & (df["airline"] == airline)]
    fig_violin.add_trace(go.Violin(y=business_data["price"], name=f'{airline} - Business'))

fig_violin.update_layout(title="Airline prices based on companies for Economy and Business class",
                         xaxis=dict(title='Class'),
                         yaxis=dict(title='Price in $'),
                         height=600,
                         width=800,
                         margin=dict(l=0, r=0, t=50, b=50),
                         autosize=False)

# Define the layout for the first page
layout = html.Div([
    html.H1('General Information About The Data', style={'color': 'navy'}),
    dcc.Graph(figure=fig_pie),  # Add the pie chart to the layout
    dcc.Graph(figure=fig_bar),  # Add the stacked bar chart to the layout
    html.Div(
        dcc.Graph(figure=fig_violin),  # Add the violin plot to the layout
        style={'display': 'flex', 'justifyContent': 'center'}
    ),
])