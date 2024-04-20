import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
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

st.markdown("## Heatmap de correlation du suicide")
st.write("""
         Coefficient proche de 1 : Il indique une corrélation positive forte, ce qui signifie que les variables évoluent généralement dans la même direction. Par exemple, si une variable augmente, l'autre a tendance à augmenter également.

         Coefficient proche de -1 : Il indique une corrélation négative forte, ce qui signifie que les variables évoluent généralement dans des directions opposées. Si une variable augmente, l'autre a tendance à diminuer, et vice versa.

         Coefficient proche de 0 : Il indique une faible corrélation linéaire entre les variables. Cela signifie que les variables ne sont pas linéairement liées les unes aux autres.""")

cat_features  = ['RegionCode','RegionName','CountryCode', 'CountryName','Sex','AgeGroup','Generation']
df.drop(columns=cat_features).corr()

fig = plt.figure(figsize=(12, 8))
sns.heatmap(df.drop(columns=cat_features).corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap de correlation')
st.pyplot(fig)

#
numeric_columns = ['DeathRatePer100K', 'GDP', 'GDPPerCapita', 'GrossNationalIncome', 'GNIPerCapita', 'InflationRate',
                  'EmploymentPopulationRatio']


max_year_suicides = df.groupby('Year')['SuicideCount'].sum().idxmax()
max_year_suicide_count = df.groupby('Year')['SuicideCount'].sum().max()


min_year_suicides = df.groupby('Year')['SuicideCount'].sum().idxmin()
min_year_suicide_count = df.groupby('Year')['SuicideCount'].sum().min()


max_generation_suicides = df.groupby('Generation')['SuicideCount'].sum().idxmax()
max_generation_suicide_count = df.groupby('Generation')['SuicideCount'].sum().max()


total_suicides_1990_2022 = df['SuicideCount'].sum()

st.title("Les taux les plus importants du suicide dans le monde")

st.markdown(f"### **Année avec le plus haut taux de suicides :** {max_year_suicides} avec un total de {max_year_suicide_count} suicides.")
st.markdown(f"### **Année avec le plus bas taux de suicides :** {min_year_suicides} avec un total de {min_year_suicide_count} suicides.")
st.markdown(f"### **Génération avec le plus haut taux de suicides :** {max_generation_suicides} avec un total de {max_generation_suicide_count} suicides.")
st.markdown(f"### **Nombre total de suicides de 1990 à 2022 :** {total_suicides_1990_2022}")