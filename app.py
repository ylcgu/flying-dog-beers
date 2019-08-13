import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart
beers=['History and the last man', 'The origin of politics', 'Principle', 'How to tell a story']
ibu_values=[30, 64, 65, 95]
abv_values=[7.4, 17.1, 8.2, 4.8]
color1='darkred'
color2='lightgrey'

bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name='IBU',
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name='ABV',
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = 'Beer Comparison'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Flying Dog Beers'),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href='https://github.com/austinlasseter/flying-dog-beers'),
    html.Br(),
    html.A('Data Source', href='https://www.flyingdog.com/beers/'),
    ]
)

if __name__ == '__main__':
    app.run_server()
