import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import plotly.express as px

df = pd.read_csv("SuicideMonde1990-2022.csv", encoding='utf-8')
conn = sqlite3.connect("suicide.db")
chart = pd.read_csv('SuicideMonde1990-2022.csv')


suicide_by_year = df.groupby('Year')['SuicideCount'].sum()

suicide_by_year.plot(kind='bar', figsize=(20,10), color='skyblue')
plt.title("Tendances des taux de suicide au fil du temps")
plt.ylabel("Nombre de suicides")
plt.xlabel('Année')
plt.show()


suicide_by_gender = df.dropna().groupby(['Sex'])['SuicideCount'].sum()

labels = ['Femme', 'Homme']
colors = ['#ff9999', '#66b3ff']
plt.figure(figsize=(8, 8))  
plt.pie(suicide_by_gender, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Taux de suicide par sexe')
plt.axis('equal') 
plt.legend(labels, loc='upper right')

plt.show()

# fig = px.choropleth(df,
#                     locations='CountryName', locationmode='country names',
#                     color = 'SuicideCount',hover_name="CountryName",
#                     animation_frame="Year",
#                     color_continuous_scale='Viridis_r')
# fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0}, coloraxis_colorbar=dict(
#     title = 'Suicide Count',
#     ticks = 'outside',
#     tickvals = [5000,10000,15000,20000,30000, 40000, 50000],
#     dtick = 12))              
# fig.show()


sdf = chart['Year']
start_date = 2015
end_date = 2022
time_filtered = chart[(chart['Year'] >= start_date) & (chart['Year'] <= end_date)]
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
plt.figure(figsize=(10, 6)) 
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

plt.show()


