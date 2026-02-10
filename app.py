from dash import Dash, html

app = Dash(__name__)
server = app.server

app.layout = html.Div(
    children=[
        html.H1("My First Dashboard"),
        html.P("This is live on the internet 🚀")
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
