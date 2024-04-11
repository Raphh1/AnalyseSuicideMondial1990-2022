from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px


df = pd.read_csv('SuicideMonde1990-2022.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Sucide in the world', style={'textAlign':'center'}),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.histogram(df, x='RegionName', y='SuicideCount', histfunc='avg'))
])

if __name__ == '__main__':
    app.run(debug=True)


#RegionCode,RegionName,CountryCode,CountryName,Year,Sex,AgeGroup,Generation,SuicideCount,CauseSpecificDeathPercentage,DeathRatePer100K,Population,GDP,GDPPerCapita,GrossNationalIncome,GNIPerCapita,InflationRate,EmploymentPopulationRatio
