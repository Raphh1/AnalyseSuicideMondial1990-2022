import pandas as pd
import sqlite3


df = pd.read_csv("SuicideMonde1990-2022.csv", encoding='utf-8')
conn = sqlite3.connect("suicide.db")
df.to_sql('suicide', conn, if_exists='replace', index=False)


conn.commit()
conn.close()
