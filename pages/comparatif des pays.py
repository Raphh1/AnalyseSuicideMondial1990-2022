import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("SuicideMonde1990-2022.csv")

st.sidebar.title("Sélection de la plage de dates")
start_date = st.sidebar.slider("Date de début", min_value=df['Year'].min(), max_value=df['Year'].max())
end_date = st.sidebar.slider("Date de fin", min_value=df['Year'].min(), max_value=df['Year'].max(), value=df['Year'].max())


time_filtered = df[(df['Year'] >= start_date) & (df['Year'] <= end_date)]


russia_data = time_filtered[time_filtered['CountryName'] == 'Russian Federation']
suicide_counts_russia = russia_data.groupby('Year')['SuicideCount'].sum()


antigua_barbuda_data = time_filtered[time_filtered['CountryName'] == 'Antigua and Barbuda']
suicide_counts_antigua_barbuda = antigua_barbuda_data.groupby('Year')['SuicideCount'].sum()


fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(suicide_counts_russia.index, suicide_counts_russia.values, color='g', label='Russian Federation')
ax.set_title('Taux de suicides annuels dans la Fédération de Russie')
ax.set_xlabel('Année')
ax.set_ylabel('Nombre de suicides')
ax.grid(True)
ax.legend()


fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(suicide_counts_antigua_barbuda.index, suicide_counts_antigua_barbuda.values, color='b', label='Antigua and Barbuda')
ax2.set_title('Taux de suicides annuels à Antigua et Barbuda')
ax2.set_xlabel('Année')
ax2.set_ylabel('Nombre de suicides')
ax2.grid(True)
ax2.legend()


st.title("Analyse des taux de suicides par pays dans le monde")

st.markdown("## La federation Russe")
st.write("""La Fédération de Russie est souvent citée comme ayant l'un des taux de suicide les plus élevés au monde pour plusieurs raisons socio-économiques et culturelles.

Tout d'abord, les conditions socio-économiques difficiles, telles que le chômage élevé, la pauvreté, les inégalités économiques et l'insécurité financière, sont des facteurs de stress majeurs qui peuvent contribuer aux pensées suicidaires et aux comportements auto-destructeurs. La transition économique tumultueuse après la dissolution de l'Union soviétique a laissé de nombreuses personnes sans emploi stable et sans filet de sécurité sociale adéquat, ce qui a alimenté les sentiments de désespoir et d'impuissance.

De plus, la consommation élevée d'alcool en Russie est un problème de santé publique majeur qui est étroitement lié aux taux de suicide élevés. L'alcoolisme chronique est souvent associé à des problèmes de santé mentale sous-jacents tels que la dépression et l'anxiété, et il peut aggraver les pensées suicidaires.

Sur le plan culturel, il existe une stigmatisation persistante associée à la santé mentale en Russie, ce qui peut dissuader les personnes en détresse de rechercher de l'aide. Les attitudes sociales et familiales autour du suicide peuvent également influencer les comportements, certains percevant encore le suicide comme une issue acceptable face à des difficultés insurmontables""")

st.pyplot(fig)

st.markdown("## Antigua et Barbuda")
st.write("""Antigua-et-Barbuda, un petit État insulaire des Caraïbes, affiche l'un des taux de suicide les plus bas au monde. Plusieurs facteurs peuvent contribuer à ce faible taux de suicide.

Tout d'abord, les conditions socio-économiques favorables, telles que le faible chômage, la stabilité économique et les niveaux relativement élevés de bien-être, peuvent créer un environnement social et économique favorable à la santé mentale et au bien-être psychologique.

De plus, les fortes communautés et les liens sociaux étroits caractéristiques des petites îles des Caraïbes peuvent offrir un soutien social et émotionnel important aux individus en période de crise ou de difficulté. Le fort sentiment d'appartenance à la communauté et le soutien familial peuvent aider à atténuer les sentiments d'isolement et de désespoir.

Enfin, les attitudes culturelles et sociales favorables à la santé mentale, ainsi que la sensibilisation accrue aux problèmes de santé mentale et au suicide, peuvent encourager les individus à rechercher de l'aide en cas de besoin et à bénéficier de services de soutien et de traitement appropriés.""")

st.pyplot(fig2)
