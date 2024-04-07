import dash
from dash import html
import sqlite3


app = dash.Dash(__name__)


conn = sqlite3.connect('youtube.db')
cursor = conn.cursor()


cursor.execute("SELECT rank, Youtuber FROM youtubers LIMIT 20")
youtubers = cursor.fetchall()

app.layout = html.Div([
    html.H1("Liste des 20 premiers Youtubeurs"),
 
    html.Ul([
        html.Li(html.A(youtubeur[1], href=f"/youtubeur/{youtubeur[0]}")) for youtubeur in youtubers
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
