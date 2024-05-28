from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('../data/flights_dataset.csv')
df = df.drop(df.columns[0], axis=1)

price_by_day = df.groupby(['days_left'])['price'].mean().reset_index()

fig_linear = px.scatter(price_by_day, x='days_left', y='price',
                        title='Flight prices based on days left before buying the ticket (Linear Regression)',
                        labels={'days_left': 'Days Left', 'price': 'Average Price'},
                        trendline="ols",
                        trendline_color_override="#79d6ae",
                        color_discrete_sequence=["#332345" if 1 < x < 20 else "#38aaac" for x in price_by_day['days_left']]
                       )

fig_linear.update_traces(marker=dict(size=15, color="#e3c310"))

# Plot with polynomial trendline
fig_poly = px.scatter(price_by_day, x='days_left', y='price',
                      title='Flight prices based on days left before buying the ticket (Polynomial Regression)',
                      labels={'days_left': 'Days Left', 'price': 'Average Price'},
                      trendline="lowess",
                      trendline_color_override="#79d6ae",
                      color_discrete_sequence=["#332345" if 1 < x < 20 else "#38aaac" for x in price_by_day['days_left']]
                     )

fig_poly.update_traces(marker=dict(size=15, color="#e3c310"))

# Define layout for the page
layout = html.Div(children=[
    html.H1(children='Flight Prices', style={'color': 'navy'}),

    dcc.Graph(
        id='price-graph-linear',
        figure=fig_linear
    ),

    dcc.Graph(
        id='price-graph-poly',
        figure=fig_poly
    )
])
