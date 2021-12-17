import pandas as pd
import csv
import plotly.express as px
import numpy as np

df = pd.read_csv("student_stats.csv")
fig = px.scatter(df, x = 'Days Present', y = 'Marks In Percentage')
fig.show()

days_present = []
marks = []

with open('student_stats.csv') as f:
    df = csv.DictReader(f)

    for row in df:
        days_present.append(float(row['Days Present']))
        marks.append(float(row['Marks In Percentage']))

correlation = np.corrcoef(days_present, marks)

print(correlation[0,1])