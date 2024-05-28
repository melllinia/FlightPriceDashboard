from dash import dcc, html, dash
import plotly.express as px
import pandas as pd
from data_loader import df
import dash.dependencies as dd


price_by_day = df.groupby(['days_left'])['price'].mean().reset_index()

# Plot with linear trendline
fig_linear = px.scatter(price_by_day, x='days_left', y='price',
                        title='Flight prices based on days left before buying the ticket',
                        labels={'days_left': 'Days Left', 'price': 'Average Price'},
                        trendline="ols",
                        trendline_color_override="#79d6ae",
                        color_discrete_sequence=["#332345" if 1 < x < 20 else "#38aaac" for x in
                                                 price_by_day['days_left']]
                        )

fig_linear.update_traces(marker=dict(size=15, color="#e3c310"))

# Plot with polynomial trendline
fig_poly = px.scatter(price_by_day, x='days_left', y='price',
                      title='Flight prices based on days left before buying the ticket',
                      labels={'days_left': 'Days Left', 'price': 'Average Price'},
                      trendline="lowess",
                      trendline_color_override="#79d6ae",
                      color_discrete_sequence=["#332345" if 1 < x < 20 else "#38aaac" for x in
                                               price_by_day['days_left']]
                      )

fig_poly.update_traces(marker=dict(size=15, color="#e3c310"))


layout = html.Div(children=[
    html.H1(children='Flight Prices', style={'color': 'navy'}),

    dcc.Dropdown(
        id='plot-type-dropdown',
        options=[
            {'label': 'Linear Trendline', 'value': 'linear'},
            {'label': 'Polynomial Trendline', 'value': 'polynomial'}
        ],
        value='linear'
    ),

    html.Div(id='output-graph')
])


def update_graph(selected_plot):
    if selected_plot == 'linear':
        return dcc.Graph(
            id='price-graph-linear',
            figure=fig_linear
        )
    elif selected_plot == 'polynomial':
        return dcc.Graph(
            id='price-graph-poly',
            figure=fig_poly
        )

def update_output(selected_plot):
    return update_graph(selected_plot)
