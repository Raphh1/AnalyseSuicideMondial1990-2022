import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


chart = pd.read_csv("SuicideMonde1990-2022.csv")  

st.title("Taux de suicides annuels en Europe (par rapport a la population complète de la region)")


st.sidebar.title("Sélection de la plage de dates")
start_date = st.sidebar.slider("Date de début", min_value=chart['Year'].min(), max_value=chart['Year'].max())
end_date = st.sidebar.slider("Date de fin", min_value=chart['Year'].min(), max_value=chart['Year'].max(), value=chart['Year'].max())


time_filtered = chart[(chart['Year'] >= start_date) & (chart['Year'] <= end_date)]
europe = time_filtered[time_filtered['RegionCode'] == 'EU']
annual_suicide_counts_europe = europe.groupby('Year')['SuicideCount'].sum()


fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(annual_suicide_counts_europe.index, annual_suicide_counts_europe.values, marker='o', linestyle='-', color='g', label='Europe')
ax.set_title('Taux de suicides annuels en Europe')
ax.set_xlabel('Année')
ax.set_ylabel('Nombre de suicides')
ax.grid(True)
ax.legend()


st.pyplot(fig)

st.write(""" L'analyse des taux de suicide élevés en Europe révèle une interconnexion complexe de facteurs socio-économiques, culturels et individuels. Au cœur de cette réalité alarmante se trouve souvent une combinaison de pressions sociales intenses, de stress économique, d'accès limité aux soins de santé mentale et d'isolement social croissant. La pression sociale omniprésente, exacerbée par des normes culturelles exigeantes et une compétition professionnelle féroce, peut peser lourdement sur les individus, en particulier les jeunes adultes et ceux en situation de précarité économique. Les défis économiques, tels que le chômage persistant et les inégalités croissantes, peuvent aggraver les sentiments d'impuissance et de désespoir, renforçant ainsi le risque de suicide. De plus, malgré la disponibilité de systèmes de santé bien développés dans de nombreux pays européens, l'accès aux soins de santé mentale reste souvent limité en raison de barrières financières, de stigmatisation et de ressources insuffisantes. L'urbanisation croissante et la mobilité accrue ont également contribué à un déclin des liens communautaires traditionnels, laissant de nombreuses personnes vulnérables à l'isolement social et à la détresse psychologique. Face à cette réalité complexe, il est impératif de développer des stratégies de prévention et d'intervention holistiques qui abordent les multiples dimensions de la crise du suicide en Europe.""")


st.title("Taux de suicides annuels en Amerique Centrale et Amerique du Sud (par rapport a la population complète de la region)")


time_filtered = chart[(chart['Year'] >= start_date) & (chart['Year'] <= end_date)]
centralamericasouth = time_filtered[time_filtered['RegionCode'] == 'CSA']
annual_suicide_counts_centralamericasouth = centralamericasouth.groupby('Year')['SuicideCount'].sum()


fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(annual_suicide_counts_centralamericasouth.index, annual_suicide_counts_centralamericasouth.values, marker='o', linestyle='-', color='y', label='Amerique centrale et amerique du sud')
ax.set_title('Taux de suicides annuels en Amerique centrale et amerique du sud')
ax.set_xlabel('Année')
ax.set_ylabel('Nombre de suicides')
ax.grid(True)
ax.legend()


st.pyplot(fig)

st.write("""L'examen des taux de suicide relativement bas en Amérique du Sud et en Amérique centrale révèle une série de facteurs socio-économiques, culturels et environnementaux qui pourraient contribuer à cette réalité. Ces régions sont souvent caractérisées par des liens communautaires forts, un soutien familial étendu et une culture qui valorise les interactions sociales et les réseaux de soutien. Les relations sociales étroites et les traditions familiales solides peuvent jouer un rôle crucial dans la protection contre l'isolement social et la détresse psychologique. De plus, la forte présence de valeurs culturelles et spirituelles peut fournir un sens de l'appartenance et de la signification, offrant ainsi une bouée de sauvetage émotionnelle pour les individus en difficulté. Sur le plan économique, bien que de nombreux pays d'Amérique du Sud et d'Amérique centrale soient confrontés à des défis socio-économiques importants, tels que la pauvreté et les inégalités, la cohésion sociale et les réseaux de soutien informels peuvent atténuer les effets de ces défis et offrir un filet de sécurité pour les individus en crise. En outre, les environnements naturels vastes et diversifiés de ces régions peuvent offrir des opportunités de connexion avec la nature et de ressourcement, ce qui peut contribuer au bien-être mental et émotionnel. En combinant ces facteurs, il est possible que les niveaux relativement faibles de suicide en Amérique du Sud et en Amérique centrale soient le résultat d'une combinaison de soutien social fort, de valeurs culturelles résilientes et d'un environnement naturel nourrissant qui favorise le bien-être émotionnel.""")