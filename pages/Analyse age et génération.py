import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SuicideMonde1990-2022.csv")


df = df[df['Generation'] != 'Unknown']


start_year = st.sidebar.slider("Année de début", min_value=1990, max_value=2022, value=1990)
end_year = st.sidebar.slider("Année de fin", min_value=start_year, max_value=2022, value=2022)


df_filtered = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]


st.title("Taux de suicides par génération dans le monde")
fig, ax = plt.subplots(figsize=(10, 6))
for generation, data in df_filtered.groupby('Generation'):
    data.groupby('Year')['SuicideCount'].sum().plot(kind='line', ax=ax, label=generation)


plt.title('Taux de suicide par génération en fonction des années')
plt.xlabel('Année')
plt.ylabel('Nombre de suicides')
plt.legend(title='Génération', loc='upper right')

st.pyplot(fig)

df_filtered = df[(df['Year'] >= 1990) & (df['Year'] <= 2022) & (df['Generation'] == 'Baby Boomers')]


st.title("Taux de suicides pour la génération Baby Boomers")
fig, ax = plt.subplots(figsize=(10, 6))
for age_group, data in df_filtered.groupby('AgeGroup'):
    data.groupby('Year')['SuicideCount'].sum().plot(kind='line', ax=ax, label=age_group)


plt.title("Taux de suicide pour la génération Baby Boomers par tranche d'âge")
plt.xlabel('Année')
plt.ylabel('Nombre de suicides')
plt.legend(title='Tranche d\'âge', loc='upper right')


st.pyplot(fig)

st.write(""" Les Baby Boomers, nés entre 1946 et 1964, ont souvent été confrontés à des périodes de changement social rapide et de turbulences économiques. Leur génération a été témoin de transformations majeures telles que l'émergence de la contre-culture des années 1960 et les défis économiques des années 1970 et 1980. Ces facteurs peuvent avoir contribué à des taux de suicide relativement élevés au sein de cette cohorte.""")

df_filtered = df[(df['Year'] >= 1990) & (df['Year'] <= 2022) & (df['Generation'] == 'Generation X')]


st.title("Taux de suicides pour la génération X")
fig, ax = plt.subplots(figsize=(10, 6))
for age_group, data in df_filtered.groupby('AgeGroup'):
    data.groupby('Year')['SuicideCount'].sum().plot(kind='line', ax=ax, label=age_group)


plt.title("Taux de suicide pour la génération X par tranche d'âge")
plt.xlabel('Année')
plt.ylabel('Nombre de suicides')
plt.legend(title='Tranche d\'âge', loc='upper right')


st.pyplot(fig)

st.write(""" La génération X, née entre les années 1960 et 1980, a été marquée par des avancées technologiques rapides, des changements sociétaux majeurs et des défis économiques. Cette génération a été confrontée à des pressions croissantes liées au travail, à la famille et à la vie sociale, ce qui pourrait expliquer les tendances variées observées dans les taux de suicide au fil du temps.""")

df_filtered_millenials = df[(df['Year'] >= 1990) & (df['Year'] <= 2022) & (df['Generation'] == 'Millennials')]


st.title("Taux de suicides pour la génération Millenials")
fig, ax = plt.subplots(figsize=(10, 6))
for age_group, data in df_filtered_millenials.groupby('AgeGroup'):
    data.groupby('Year')['SuicideCount'].sum().plot(kind='line', ax=ax, label=age_group)


plt.title("Taux de suicide pour la génération Millenials par tranche d'âge")
plt.xlabel('Année')
plt.ylabel('Nombre de suicides')
plt.legend(title='Tranche d\'âge', loc='upper right')


st.pyplot(fig)

st.write(""" Les Milléniaux, nés entre les années 1980 et le début des années 2000, ont été façonnés par l'avènement d'Internet, la mondialisation et les réseaux sociaux. Bien que souvent perçue comme une génération technologiquement avancée et socialement consciente, les Milléniaux peuvent également faire face à des défis tels que le chômage, les dettes étudiantes élevées et les pressions sociales accrues, qui peuvent contribuer aux taux de suicide.""")



df_filtered = df[(df['Year'] >= 2000) & (df['Generation'] == 'Generation Z')]


st.title("Taux de suicides pour la génération Z")
fig, ax = plt.subplots(figsize=(10, 6))
df_filtered.groupby('Year')['SuicideCount'].sum().plot(kind='line', ax=ax)


plt.title("Taux de suicide pour la génération Z")
plt.xlabel('Année')
plt.ylabel('Nombre de suicides')


st.pyplot(fig)

st.write(""" La génération Z, née au début des années 2000 et au-delà, est encore en train de se former, mais des études initiales suggèrent des défis uniques, notamment une utilisation précoce et intensive des médias sociaux, des niveaux élevés de stress liés à la performance et des incertitudes quant à l'avenir économique et environnemental. Ces facteurs pourraient influencer les tendances futures du suicide au sein de cette cohorte.""")

df_filtered_silent = df[(df['Year'] >= 1990) & (df['Generation'] == 'Silent Generation')]


st.title("Taux de suicides pour la génération Silencieuse")
fig, ax = plt.subplots(figsize=(10, 6))
for age_group, data in df_filtered_silent.groupby('AgeGroup'):
    data.groupby('Year')['SuicideCount'].sum().plot(kind='line', ax=ax, label=age_group)


plt.title("Taux de suicide pour la génération Silencieuse par tranche d'âge")
plt.xlabel('Année')
plt.ylabel('Nombre de suicides')
plt.legend(title='Tranche d\'âge', loc='upper right')


st.pyplot(fig)
st.write("""Enfin, la génération silencieuse, née avant les années 1940, a été influencée par des événements historiques tels que la Grande Dépression et les guerres mondiales. Bien que souvent moins étudiée que d'autres générations plus récentes, la génération silencieuse a également été confrontée à des défis significatifs qui ont pu avoir un impact sur les taux de suicide.""")


df_filtered_alpha = df[(df['Year'] >= 2010) & (df['Generation'] == 'Generation Alpha')]


st.title("Taux de suicides pour la génération Alpha")
fig, ax = plt.subplots(figsize=(10, 6))
for age_group, data in df_filtered_alpha.groupby('AgeGroup'):
    data.groupby('Year')['SuicideCount'].sum().plot(kind='line', ax=ax, label=age_group)


plt.title("Taux de suicide pour la génération Alpha par tranche d'âge")
plt.xlabel('Année')
plt.ylabel('Nombre de suicides')
plt.legend(title='Tranche d\'âge', loc='upper right')


st.pyplot(fig)

st.write("""la génération Alpha, qui désigne les individus nés à partir de 2010 environ, est une génération relativement récente et peu de données peuvent être disponibles sur leur comportement en matière de suicide.""")