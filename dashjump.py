import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

# To make your element perform a "hinge" animation, 
# you just need to replace animate__bounce with animate__hinge in 
# the className parameter. 
# This will apply the hinge animation from the Animate.css library.

app.layout = html.Div(
    children=[
        html.Div(
            "I will bounce",
            id="output",
            className="animate__animated animate__hinge animate__infinite",  # Animate.css classes
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
