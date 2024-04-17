


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("SuicideMonde1990-2022.csv") 


st.title('Corrélation entre le taux de suicides et le taux d\'inflation en Amérique du Nord')


st.sidebar.title("Sélection de la plage de dates")
start_date = st.sidebar.slider("Date de début", min_value=df['Year'].min(), max_value=df['Year'].max())
end_date = st.sidebar.slider("Date de fin", min_value=df['Year'].min(), max_value=df['Year'].max(), value=df['Year'].max())


time_filtered = df[(df['Year'] >= start_date) & (df['Year'] <= end_date)]


region = st.sidebar.selectbox("Choisissez une région", time_filtered['RegionName'].unique())


region_data = time_filtered[time_filtered['RegionName'] == region]


suicide_by_year = region_data.groupby('Year')['SuicideCount'].sum()
employment_by_year = region_data.groupby('Year')['EmploymentPopulationRatio'].mean()


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
ax2.plot(employment_by_year.index, employment_by_year.values, marker='s', linestyle='--', color=color, label='Taux d\'emploi')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')

fig.tight_layout()  


st.pyplot(fig)


inflation_by_year = region_data.groupby('Year')['InflationRate'].mean()


fig2, ax3 = plt.subplots(figsize=(10, 6))


color = 'tab:red'
ax3.set_xlabel('Année')
ax3.set_ylabel('Taux de suicides', color=color)
ax3.plot(suicide_by_year.index, suicide_by_year.values, marker='o', linestyle='-', color=color, label='Taux de suicides')
ax3.tick_params(axis='y', labelcolor=color)
ax3.legend(loc='upper left')


ax4 = ax3.twinx()  
color = 'tab:blue'
ax4.set_ylabel('Taux d\'inflation', color=color)  
ax4.plot(inflation_by_year.index, inflation_by_year.values, marker='s', linestyle='--', color=color, label='Taux d\'inflation')
ax4.tick_params(axis='y', labelcolor=color)
ax4.legend(loc='upper right')

fig2.tight_layout()  


st.pyplot(fig2)
