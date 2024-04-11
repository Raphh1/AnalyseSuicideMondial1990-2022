import pandas as pd
import sqlite3


df = pd.read_csv("GlobalYouTubeStatistics.csv", encoding='latin1')
conn = sqlite3.connect("youtube.db")
df.to_sql('youtubers', conn, if_exists='replace', index=False)



conn.commit()
conn.close()
