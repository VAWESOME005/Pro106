import pandas as pd
import csv
import plotly.express as px
import numpy as np

df = pd.read_csv("coffee_sleep.csv")
fig = px.scatter(df, x = 'Coffee in ml', y = 'sleep in hours')
fig.show()

coffee = []
sleep = []
with open("coffee_sleep.csv") as f:
    df = csv.DictReader(f)
    for row in df:
        coffee.append(float(row['Coffee in ml']))
        sleep.append(float(row['sleep in hours']))

correlation = np.corrcoef(coffee, sleep)

print(correlation[0,1])