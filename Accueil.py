import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import json

 
st.write("""
         # Article sur le suicide dans le monde

         Dans cet article, nous entreprenons une analyse approfondie des tendances du suicide à travers les continents et les pays, en utilisant des données clés telles que les tranches d'âge, les générations, le taux d'inflation et le ratio d'emploi. Bien que ces données ne soient pas spécifiquement liées au suicide, elles peuvent fournir des indications importantes sur les facteurs socio-économiques qui influent sur les taux de suicide.
""")

 
df = pd.read_csv("SuicideMonde1990-2022.csv")

st.write(""" 
         ## Taux de suicides par sexes
         
        L'un des aspects les plus significatifs des tendances du suicide est la disparité entre les sexes. Les hommes ont tendance à avoir des taux de suicide plus élevés que les femmes dans de nombreux pays du monde. Cette disparité peut être influencée par une variété de facteurs, y compris les différences dans les méthodes de suicide choisies et les normes de genre qui affectent la manière dont les hommes et les femmes expriment leur détresse émotionnelle.
         """)


gender_sum = df.dropna().groupby(['Sex'])['SuicideCount'].sum()

fig, ax = plt.subplots(figsize=(5, 5))

colors = ['#ff9999', '#66b3ff']
labels = ['Female', 'Male']

wedgeprops = dict(width=0.6, edgecolor='w', linewidth=2)
ax.pie(
    gender_sum,
    labels=labels,
    autopct='%.1f%%',
    colors=colors,
    startangle=90,
    counterclock=False,
    wedgeprops=wedgeprops,
)

ax.set_title(
    'Suicide by Gender',
    fontdict={'fontsize': 16, 'fontweight': 'bold', 'color': '#333333'},
)

ax.axis('off') 

st.pyplot(fig)


st.write(""" 
         ## Taux de suicides dans le monde

         Le taux de suicide varie considérablement d'un pays à l'autre et d'une région à l'autre. Cette variation peut être due à des différences dans les facteurs socio-économiques, culturels, géographiques et politiques. Comprendre ces variations régionales est essentiel pour élaborer des stratégies de prévention du suicide efficaces et adaptées à chaque contexte.
         """)

suicide_by_year = df.groupby('Year')['SuicideCount'].sum()

figu = plt.figure()
suicide_by_year.plot(kind='bar', figsize=(10,5), color='skyblue')
plt.title("Tendances des taux de suicide au fil du temps")
plt.ylabel("Nombre de suicides")
plt.xlabel('Année')
st.pyplot(figu)

st.write(""" 
         ## Taux de suicide par région

         En examinant les taux de suicide par région, nous pouvons identifier des tendances et des disparités significatives. Par exemple, l'Amérique centrale et l'Amérique du Sud affichent généralement des taux de suicide plus bas que d'autres régions du monde, tandis que l'Europe et certaines parties de l'Asie ont des taux de suicide plus élevés. Comprendre ces variations régionales peut fournir des indications importantes pour la prévention du suicide à l'échelle mondiale.
         """)

st.title("Taux de suicides annuels par région")


start_date = df['Year'].min()
end_date = df['Year'].max()


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


fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(annual_suicide_counts_asia.index, annual_suicide_counts_asia.values, marker='o', linestyle='-', color='b', label='Asia')  
ax.plot(annual_suicide_counts_africa.index, annual_suicide_counts_africa.values, marker='o', linestyle='-', color='r', label='Africa')  
ax.plot(annual_suicide_counts_europe.index, annual_suicide_counts_europe.values, marker='o', linestyle='-', color='g', label='Europe') 
ax.plot(annual_suicide_counts_northamerica.index, annual_suicide_counts_northamerica.values, marker='o', linestyle='-', color='y', label='North America')
ax.plot(annual_suicide_counts_centralsouthamerica.index, annual_suicide_counts_centralsouthamerica.values, marker='o', linestyle='-', color='purple', label='Central and South America')     
ax.set_title('Taux de suicides annuels par région')
ax.set_xlabel('Année')
ax.set_ylabel('Nombre de suicides')
ax.grid(True)
ax.legend()


st.pyplot(fig)

#RegionCode,RegionName,CountryCode,CountryName,Year,Sex,AgeGroup,Generation,SuicideCount,CauseSpecificDeathPercentage,DeathRatePer100K,Population,GDP,GDPPerCapita,GrossNationalIncome,GNIPerCapita,InflationRate,EmploymentPopulationRatio

import plotly.express as px

fig = px.choropleth(df,
                    locations='CountryName', locationmode='country names',
                    color = 'SuicideCount',hover_name="CountryName",
                    animation_frame="Year",
                    color_continuous_scale='Viridis_r')
fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0}, coloraxis_colorbar=dict(
    title = 'Suicide Count',
    ticks = 'outside',
    tickvals = [5000,10000,15000,20000,30000, 40000, 50000],
    dtick = 12))              
st.plotly_chart(fig)