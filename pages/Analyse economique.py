


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SuicideMonde1990-2022.csv")

st.sidebar.title("Sélection de la plage de dates")
start_date = st.sidebar.slider("Date de début", min_value=df['Year'].min(), max_value=df['Year'].max())
end_date = st.sidebar.slider("Date de fin", min_value=df['Year'].min(), max_value=df['Year'].max(), value=df['Year'].max())

time_filtered = df[(df['Year'] >= start_date) & (df['Year'] <= end_date)]

region = st.sidebar.selectbox("Choisissez une région", time_filtered['RegionName'].unique())

region_data = time_filtered[time_filtered['RegionName'] == region]

suicide_by_year = region_data.groupby('Year')['SuicideCount'].sum()
employment_by_year = region_data.groupby('Year')['EmploymentPopulationRatio'].mean()


if region == 'Europe':
    st.title("Analyse des taux de suicide en fonction du taux d'emploi et du taux d'inflation en Europe \n ## (population complète de la region)")
    st.markdown("## Taux de suicide par rapport au taux d'emploi")
    st.write("Dans de nombreux pays européens, il existe une relation inverse entre le taux de chômage et le taux d’emploi. Plus il y a de chômeurs, plus le taux d’emploi est faible, et vice versa. Cette corrélation peut sembler logique : lorsque le chômage augmente, la pression sur l’emploi s’intensifie, ce qui peut affecter la santé mentale des individus.")
    st.write("En France, par exemple, le taux d’emploi évolue lentement, passant d’environ 10 % à 8,6 %. Cependant, la France n’est toujours pas bien placée en Europe en termes de productivité et de conditions de travail. Un taux d’emploi et une durée de travail faibles ont entraîné une baisse de la productivité, plaçant la France au 29e rang.")
    st.markdown("## Taux de suicide par rapport au taux d'inflation")
    st.write("L’inflation peut également jouer un rôle dans la santé mentale. Des périodes d’inflation élevée peuvent entraîner des incertitudes économiques, des perturbations sociales et des tensions psychologiques, pouvant contribuer aux taux de suicide.Cependant, il est important de noter que la relation entre l’inflation et le suicide est complexe et dépend de nombreux autres facteurs socio-économiques.")

elif region == 'Asia':
    st.title("Analyse des taux de suicide en fonction du taux d'emploi et du taux d'inflation en Asie \n ## (population complète de la region)")
    st.markdown("## Taux de suicide par rapport au taux d'emploi")
    st.write("L'examen des tendances du taux de suicides en Asie révèle une corrélation complexe avec le taux d'emploi dans la région. Alors que des données spécifiques sont nécessaires pour une analyse approfondie, des études antérieures suggèrent une relation bidirectionnelle entre le taux de suicides et le taux d'emploi en Asie. D'une part, un faible taux d'emploi peut contribuer à des niveaux accrus de détresse économique, de stress et de désespoir parmi les individus, augmentant ainsi le risque de suicide. D'autre part, un marché du travail dynamique et compétitif peut également exercer des pressions significatives sur les individus, les poussant à l'épuisement professionnel et à des problèmes de santé mentale, ce qui peut également influencer les taux de suicides. Il est important de noter que les défis socio-économiques, culturels et démographiques varient considérablement d'un pays à l'autre en Asie, ce qui peut entraîner des variations significatives dans les facteurs de risque de suicide d'une région à l'autre. Par conséquent, une approche contextuelle et nuancée est nécessaire pour comprendre pleinement la relation entre le taux de suicides et le taux d'emploi en Asie, ainsi que pour élaborer des politiques et des interventions de prévention efficaces dans la région.")
    st.markdown("## Taux de suicide par rapport au taux d'inflation")
    st.write("Lorsqu'on examine les données du taux de suicides en relation avec le taux d'inflation en Asie, des tendances intéressantes émergent. Contrairement à d'autres régions où des fluctuations significatives du taux d'inflation peuvent avoir un impact sur les conditions économiques et, par extension, sur les niveaux de stress et de désespoir de la population, l'Asie présente souvent des taux d'inflation relativement stables. Malgré cette stabilité, le taux de suicides en Asie peut encore connaître une augmentation progressive au fil des années. Cela suggère que, bien que le taux d'inflation puisse ne pas être un facteur déterminant du taux de suicides dans la région, d'autres facteurs socio-économiques, culturels et psychologiques peuvent jouer un rôle plus important. Par exemple, des pressions sociales et familiales, des normes culturelles, des troubles mentaux non diagnostiqués et des obstacles à l'accès aux services de santé mentale peuvent tous contribuer aux taux de suicides en Asie. Par conséquent, une approche holistique est nécessaire pour comprendre les déterminants du suicide dans la région et pour élaborer des stratégies efficaces de prévention et de soutien.")
    
elif region == 'Central and South America':
    st.title("Analyse des taux de suicide en fonction du taux d'emploi et du taux d'inflation en Amérique du Sud et Amerique Centrale\n ## (population complète de la region)")
    st.markdown("## Taux de suicide par rapport au taux d'emploi")
    st.write("En examinant les données du taux de suicides en Amérique du Sud et centrale sur une période de 32 ans, entre 1990 et 2022, une corrélation significative entre le taux de suicides et le taux d'emploi émerge. Lorsque le taux d'emploi augmente, le taux de suicides semble également augmenter, suggérant un lien entre la situation économique et la santé mentale dans ces régions. Cette corrélation souligne l'importance des facteurs socio-économiques dans la prévalence du suicide, mettant en lumière la nécessité de politiques visant à soutenir l'emploi et à fournir un accès adéquat aux services de santé mentale.")
    st.markdown("## Taux de suicide par rapport au taux d'inflation")
    st.write("En revanche, l'analyse du taux de suicides par rapport au taux d'inflation révèle une dynamique différente. Malgré la stabilité du taux d'inflation à un niveau relativement bas au cours de la période étudiée, le taux de suicides continue d'augmenter progressivement. Cette observation suggère que d'autres facteurs, en dehors des pressions économiques mesurées par le taux d'inflation, peuvent influencer le taux de suicides. Des recherches supplémentaires sont nécessaires pour comprendre pleinement les déterminants du suicide dans ces régions et pour développer des interventions efficaces de prévention.")
    
elif region == 'Oceania':
    st.title("Analyse des taux de suicide en fonction du taux d'emploi et du taux d'inflation en Oceanie \n ## (population complète de la region)")
    st.markdown("## Taux de suicide par rapport au taux d'emploi")
    st.write("L'analyse des tendances du taux de suicides en Océanie révèle une corrélation significative avec le taux d'emploi dans la région. Alors que les données spécifiques peuvent varier selon les pays de l'Océanie, des études antérieures suggèrent que les défis socio-économiques, tels que le chômage, la précarité de l'emploi et les inégalités économiques, peuvent jouer un rôle important dans la prévalence du suicide. Dans de nombreux pays océaniens, les communautés autochtones sont confrontées à des taux de chômage plus élevés et à des conditions socio-économiques défavorables, ce qui peut augmenter le risque de détresse psychologique et de suicide. De plus, la géographie isolée de nombreux territoires insulaires de l'Océanie peut limiter l'accès aux services de santé mentale et de soutien, exacerbant ainsi les facteurs de risque de suicide. Par conséquent, des politiques et des programmes visant à soutenir l'emploi, à réduire les inégalités socio-économiques et à fournir un accès équitable aux services de santé mentale sont essentiels pour prévenir le suicide en Océanie.")
    st.markdown("## Taux de suicide par rapport au taux d'inflation")
    st.write("Lorsqu'on examine les données du taux de suicides en relation avec le taux d'inflation en Océanie, des tendances variées émergent, notamment en ce qui concerne la volatilité du taux d'inflation. Contrairement à d'autres régions où le taux d'inflation peut rester relativement stable, de nombreux pays océaniens peuvent connaître des fluctuations significatives du taux d'inflation au fil des années. Ces variations peuvent être attribuées à une série de facteurs économiques, géopolitiques et environnementaux propres à la région. Malgré cette volatilité, le taux de suicides en Océanie peut encore présenter une tendance à la hausse au fil du temps. Cette observation suggère que d'autres facteurs, tels que les pressions sociales, les changements démographiques et les problèmes de santé mentale non traités, peuvent jouer un rôle plus important dans la prévalence du suicide dans la région que le seul taux d'inflation. Ainsi, une approche globale de la prévention du suicide en Océanie devrait tenir compte de ces facteurs multiples et des fluctuations du contexte économique et social pour être efficace.")
    
elif region == 'North America and the Caribbean':
    st.title("Analyse des taux de suicide en fonction du taux d'emploi et du taux d'inflation en Amérique du nord et Caraibes \n ## (population complète de la region)")
    st.markdown("## Taux de suicide par rapport au taux d'emploi")
    st.write("L'examen des tendances du taux de suicides en Amérique du Nord et dans les Caraïbes révèle une corrélation complexe avec le taux d'emploi dans la région. En observant le graphique du taux d'emploi sur la période de 1990 à 2022, une augmentation significative est remarquée jusqu'en 2008, suivie d'une légère baisse et d'une stabilisation par la suite. Cette évolution peut être attribuée à une variété de facteurs économiques, politiques et sociaux, notamment les cycles économiques, les politiques gouvernementales et les changements démographiques. Cependant, malgré ces fluctuations du taux d'emploi, le taux de suicides dans la région reste relativement élevé mais ne semble pas augmenter de manière significative au fil des années. Cette observation suggère que d'autres facteurs que le taux d'emploi peuvent jouer un rôle prépondérant dans la prévalence du suicide dans la région. Parmi ces facteurs, on peut citer les troubles de santé mentale, les pressions sociales, les inégalités économiques et l'accès aux services de santé mentale. Par conséquent, une approche intégrée et holistique est nécessaire pour comprendre pleinement les déterminants du suicide en Amérique du Nord et dans les Caraïbes et pour élaborer des stratégies de prévention efficaces.")
    st.markdown("## Taux de suicide par rapport au taux d'inflation")
    st.write("Lorsqu'on examine les données du taux de suicides en relation avec le taux d'inflation en Amérique du Nord et dans les Caraïbes, on observe des fluctuations du taux d'inflation au fil des années. Contrairement à d'autres régions où le taux d'inflation peut rester relativement stable, l'Amérique du Nord et les Caraïbes connaissent des oscillations périodiques du taux d'inflation, avec des périodes où il augmente et d'autres où il diminue. Ces variations peuvent être influencées par une gamme de facteurs économiques, politiques et environnementaux, tels que les politiques monétaires, les prix des matières premières et les crises économiques régionales. Malgré ces fluctuations du taux d'inflation, le taux de suicides dans la région semble rester globalement constant au fil du temps, sans augmenter de manière significative malgré les changements économiques. Cette observation suggère que d'autres facteurs, tels que les problèmes de santé mentale, les pressions sociales et les inégalités économiques, peuvent jouer un rôle plus important dans la prévalence du suicide que le seul taux d'inflation. Ainsi, une approche intégrée de la prévention du suicide en Amérique du Nord et dans les Caraïbes devrait tenir compte de ces facteurs multiples pour élaborer des stratégies de prévention efficaces.")
    
elif region == 'Africa':
    st.title("Analyse des taux de suicide en fonction du taux d'emploi et du taux d'inflation en Afrique \n ## (population complète de la region)")
    st.markdown("## Taux de suicide par rapport au taux d'emploi")
    st.write("L'analyse du taux de suicides en relation avec le taux d'emploi en Afrique est complexe en raison de divers facteurs socio-économiques et de la disponibilité limitée de données fiables. En Afrique, le taux d'emploi peut être influencé par des problèmes tels que le chômage élevé, la précarité de l'emploi et l'économie informelle. Ces défis économiques peuvent contribuer au stress financier et à l'instabilité économique, ce qui peut affecter la santé mentale et le bien-être des individus. Cependant, les données sur le taux de suicides liés au taux d'emploi en Afrique sont souvent fragmentaires, ce qui rend difficile l'évaluation précise de cette relation. Malgré ces limitations, il est crucial de reconnaître l'importance du travail décent et de l'emploi stable pour promouvoir la santé mentale et réduire les risques de suicide dans la région.")
    st.markdown("## Taux de suicide par rapport au taux d'inflation")
    st.write("En Afrique, les données sur l'inflation peuvent être limitées, mais les problèmes potentiels d'inflation peuvent avoir des répercussions sur la population. Les pressions économiques résultant de l'inflation, telles que l'augmentation du coût de la vie et la diminution du pouvoir d'achat, peuvent accroître les tensions sociales et les difficultés financières. Cependant, les données sur le taux de suicides en Afrique sont souvent incomplètes, ce qui rend difficile l'établissement de liens directs entre le taux de suicides et le taux d'inflation. Malgré ces défis, il est crucial de reconnaître l'impact des pressions économiques sur la santé mentale et le bien-être des populations africaines.")
   



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
