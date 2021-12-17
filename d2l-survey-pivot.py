# Pivots individual attempts survey report from D2L so that Likert questions 
# (using a scale of 1 to 5) are in columns instead of rows

import pandas as pd
import numpy as np

df = pd.read_csv('survey-report.csv')

df = df.iloc[:, [0,7,8,9]]
df.columns = ['Students', 'Questions', 'Answers', 'Num_Responses']
df = df[df.Num_Responses != 0.0]
df[df.Students == ""] = np.NaN
df.Students = df.Students.ffill()
df.dropna(subset=['Questions'], inplace=True)

table = pd.pivot_table(df, values='Answers', index='Students', columns='Questions', aggfunc=np.mean)

table.to_csv('survey-pivoted.csv')
