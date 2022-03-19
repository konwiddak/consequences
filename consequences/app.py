from dash import Dash, html, dcc
from layout import base_layout

app = Dash(__name__)

app.layout = base_layout

if __name__ == '__main__':
    # visit http://127.0.0.1:8050/ in your web browser
    app.run_server(debug=True)