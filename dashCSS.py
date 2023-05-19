import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

colors = ['red', 'green', 'blue', 'yellow', 'orange']

app.layout = html.Div([
    dcc.Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0
    ),
    html.H1(id='animated-text', children='Animated Text')
])

@app.callback(
    Output('animated-text', 'style'),
    Input('interval-component', 'n_intervals'))
def update_style(n):
    return {'color': colors[n % len(colors)]}

if __name__ == '__main__':
    app.run_server(debug=True)
