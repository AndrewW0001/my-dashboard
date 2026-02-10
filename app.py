from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# --------------------
# Fake executive data
# --------------------
kpis = {
    "Revenue (YTD)": "SAR 12.4M",
    "Pipeline": "SAR 38.6M",
    "Deals Closed": "27",
    "Win Rate": "41%"
}

chart_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue (SAR M)": [1.2, 1.8, 2.1, 2.5, 2.2, 2.6]
})

fig = px.line(
    chart_data,
    x="Month",
    y="Revenue (SAR M)",
    title="Revenue Trend"
)

# --------------------
# App
# --------------------
app = Dash(__name__)
server = app.server

app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "padding": "40px",
        "backgroundColor": "#f5f7fa"
    },
    children=[

        html.H1("Executive Dashboard", style={"marginBottom": "10px"}),
        html.P("High-level performance overview", style={"color": "#555"}),

        # KPI ROW
        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)",
                "gap": "20px",
                "marginTop": "30px"
            },
            children=[
                html.Div([
                    html.H3(label),
                    html.H2(value)
                ], style={
                    "backgroundColor": "white",
                    "padding": "20px",
                    "borderRadius": "8px",
                    "boxShadow": "0 2px 6px rgba(0,0,0,0.1)"
                }) for label, value in kpis.items()
            ]
        ),

        # CHART
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "8px",
                "boxShadow": "0 2px 6px rgba(0,0,0,0.1)",
                "marginTop": "40px"
            },
            children=[
                dcc.Graph(figure=fig)
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
