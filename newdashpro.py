import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("""
         # My first app""")

chart = pd.read_csv("SuicideMonde1990-2022.csv") 
start_date = st.slider("Choisissez l'année de début", min_value=2015, max_value=2022, value=2015)
end_date = st.slider("Choisissez l'année de fin", min_value=2015, max_value=2022, value=2022)

time_filtered = chart[(chart['Year'] >= start_date) & (chart['Year'] <= end_date)]


annual_suicide_counts = time_filtered.groupby(['Year', 'RegionCode'])['SuicideCount'].sum().unstack()


st.title('Taux de suicides annuels par région')
plt.figure(figsize=(10, 6)) 
for column in annual_suicide_counts.columns:
    plt.plot(annual_suicide_counts.index, annual_suicide_counts[column], marker='o', linestyle='-', label=column)

plt.title('Taux de suicides annuels par région')
plt.xlabel('Année')
plt.ylabel('Nombre de suicides')
plt.grid(True)  
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.legend()

st.pyplot()


suicide_by_generation = chart.dropna().groupby(['Generation'])['SuicideCount'].sum()


labels = ['Baby Boomers', 'Alpha', 'X', 'Z', 'Millenials', 'Silent']
colors = ['#FF0000', '#004DFF', '#26FFB3', '#3D465B', '#FA0094', '#004C31']


st.title('Taux de suicide par génération')
plt.figure(figsize=(8, 8))  
plt.pie(suicide_by_generation, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Taux de suicide par génération')
plt.axis('equal') 
plt.legend(labels, loc='upper right')


st.pyplot()


nac_data = chart[chart['RegionCode'] == 'NAC']

suicide_by_year = nac_data.groupby('Year')['SuicideCount'].sum()
inflation_by_year = nac_data.groupby('Year')['InflationRate'].mean()


st.title('Corrélation entre le taux de suicides et le taux d\'inflation en Amérique du Nord')
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

