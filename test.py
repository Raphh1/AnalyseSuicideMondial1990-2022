import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import json

 
st.write("""
# My first app
""")
 
df = pd.read_csv("SuicideMonde1990-2022.csv")

suicide_by_gender = df.dropna().groupby(['Sex'])['SuicideCount'].sum()

labels = ['Femme', 'Homme']
colors = ['#FF0000', '#004DFF']

fig, ax = plt.subplots(figsize=(8, 8))  
ax.pie(suicide_by_gender, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax.set_title('Taux de suicide par sexe') 

st.pyplot(fig)

suicide_by_year = df.groupby('Year')['SuicideCount'].sum()

figu = plt.figure()
suicide_by_year.plot(kind='bar', figsize=(10,5), color='skyblue')
plt.title("Tendances des taux de suicide au fil du temps")
plt.ylabel("Nombre de suicides")
plt.xlabel('Année')
st.pyplot(figu)

sdf = df['Year']
start_date = 2015
end_date = 2022
time_filtered = df[(df['Year'] >= start_date) & (df['Year'] <= end_date)]
asia = time_filtered[time_filtered['RegionCode'] == 'AS']
africa = time_filtered[time_filtered['RegionCode'] == 'AF']
europe = time_filtered[time_filtered['RegionCode'] == 'EU']
centralsouthamerica = time_filtered[time_filtered['RegionCode'] == 'CSA']
northamerica = time_filtered[time_filtered['RegionCode'] == 'NAC']
annual_suicide_counts_asia = asia.groupby('Year')['SuicideCount'].sum()
annual_suicide_counts_africa = africa.groupby('Year')['SuicideCount'].sum()
annual_suicide_counts_europe = europe.groupby('Year')['SuicideCount'].sum()
annual_suicide_counts_northamerica = northamerica.groupby('Year')['SuicideCount'].sum()
annual_suicide_counts_centralsouthamerica = centralsouthamerica.groupby('Year')['SuicideCount'].sum()
figur = plt.figure(figsize=(10, 6)) 
plt.plot(annual_suicide_counts_asia.index, annual_suicide_counts_asia.values, marker='o', linestyle='-', color='b', label='Asia')  
plt.plot(annual_suicide_counts_africa.index, annual_suicide_counts_africa.values, marker='o', linestyle='-', color='r', label='Africa')  
plt.plot(annual_suicide_counts_europe.index, annual_suicide_counts_europe.values, marker='o', linestyle='-', color='g', label='Europe') 
plt.plot(annual_suicide_counts_northamerica.index, annual_suicide_counts_northamerica.values, marker='o', linestyle='-', color='y', label='North America')
plt.plot(annual_suicide_counts_centralsouthamerica.index, annual_suicide_counts_centralsouthamerica.values, marker='o', linestyle='-', color='purple', label='Central and South America')     
plt.title('Taux de suicides annuels par région')
plt.xlabel('Year')
plt.ylabel('Suicide Count')
plt.grid(True)  
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.legend()  
st.pyplot(figur)

st.title('Corrélation entre le taux de suicides et le taux d\'inflation en Amérique du Nord')


region = st.selectbox("Choisissez une région", time_filtered['RegionCode'].unique())
nac_data = df[df['RegionCode'] == region]
suicide_by_year = nac_data.groupby('Year')['SuicideCount'].sum()
inflation_by_year = nac_data.groupby('Year')['EmploymentPopulationRatio'].mean()
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Année')
ax1.set_ylabel('Taux de suicides', color=color)
ax1.plot(suicide_by_year.index, suicide_by_year.values, marker='o', linestyle='-', color=color, label='Taux de suicides')
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Taux d\'emploi', color=color)  
ax2.plot(inflation_by_year.index, inflation_by_year.values, marker='s', linestyle='--', color=color, label='Taux d\'emploi')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

fig.tight_layout()  

st.pyplot(fig)

nac_data = df[df['RegionCode'] == region]
suicide_by_year = nac_data.groupby('Year')['SuicideCount'].sum()
inflation_by_year = nac_data.groupby('Year')['InflationRate'].mean()
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Année')
ax1.set_ylabel('Taux de suicides', color=color)
ax1.plot(suicide_by_year.index, suicide_by_year.values, marker='o', linestyle='-', color=color, label='Taux de suicides')
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Taux d\'inflation', color=color)  
ax2.plot(inflation_by_year.index, inflation_by_year.values, marker='s', linestyle='--', color=color, label='Taux d\'inflation')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

fig.tight_layout()  

st.pyplot(fig)

with open("countries.geo.json") as response:
    geo = json.load(response)

fig = go.Figure(
    go.Choroplethmapbox(
        geojson=geo,
        locations=df['CountryCode'],
        featureidkey="id",
        z=df.groupby(['CountryCode'])['SuicideCount'].sum(),
        colorscale="sunsetdark",
        # zmin=0,
        # zmax=500000,
        marker_opacity=0.5,
        marker_line_width=0,
    )
)
fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=6.6,
    mapbox_center={"lat": 46.8, "lon": 8.2},
    width=800,
    height=600,
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.plotly_chart(fig)
#RegionCode,RegionName,CountryCode,CountryName,Year,Sex,AgeGroup,Generation,SuicideCount,CauseSpecificDeathPercentage,DeathRatePer100K,Population,GDP,GDPPerCapita,GrossNationalIncome,GNIPerCapita,InflationRate,EmploymentPopulationRatio
