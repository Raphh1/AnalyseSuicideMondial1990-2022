import sqlite3
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("GlobalYouTubeStatistics.csv", encoding='latin1')
conn = sqlite3.connect("youtube.db")

