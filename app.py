# app.py

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import flask
import pandas as pd

server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)

jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.H3("Big Pharma Industry", className="display-3"),
                html.P(
                    "The purpose for this is wedsite to provide information so people can form their own opinion on popular topics."
                    "The site makes no assumptions or conclusions.  Rather, it consolidates data from multiple sources and "
                    "displays it in easy to analyze visuals.  This complete project with all data is availble on github at "
                    "https://github.com/SaltyCoco/MeyitaAnalyticsDashboard.git",
                    className="lead",
                ),
                html.P(
                    "This dashboard dispays metrics for pharmasutical organizations which are incorporated within the United States. "
                    "The main metrics look at revenue, net income and employee ratings.",
                    className="lead",
                ),
            ],
            fluid=True,
        )
    ],
    fluid=True
)

app.layout = html.Div(children=[
    jumbotron
])


if __name__ == '__main__':
    app.run_server()
