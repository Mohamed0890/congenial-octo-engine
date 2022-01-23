import csv
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("amz.csv")
fig=ff.create_distplot([df["Avg"].tolist()],["Average Rating"])
fig.show()