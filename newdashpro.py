import dash
from dash import html
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

app = dash.Dash(__name__)


conn = sqlite3.connect('suicide.db')
cursor = conn.cursor()
df = pd.read_csv("SuicideMonde1990-2022.csv", encoding='utf-8')


app.layout = html.Div([
    html.H1("Liste des 20 premiers Youtubeurs"),
 
    html.Ul([
        html.Li(html.A(youtubeur[1], href=f"/youtubeur/{youtubeur[0]}")) for youtubeur in youtubers
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)


