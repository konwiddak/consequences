from dash import Dash, html, dcc
from dash_canvas import DashCanvas

base_layout = html.Div(children=[
    html.H1(children='Consequential'),
    DashCanvas(id='view_canvas', width=600, height=600),
    DashCanvas(id='draw_canvas', width=600, height=600)
])
