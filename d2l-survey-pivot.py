# Pivots individual attempts survey report from D2L so that Likert questions are in columns instead of rows
# Update paths to where your CSV file is located on your computer and where you want to save the new file

import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/username/Desktop/survey-report.csv')
df = df.iloc[:, [0,7,8,9]] # use only four columns in dataframe
df.columns = ['Students', 'Questions', 'Answers', 'Num_Responses']
df = df[df.Num_Responses' != 0.0] # remove rows where response is 0
df[df.Students == ""] = np.NaN # replace empty cells with NaN
df.Students = df.Students.ffill() # flash fill students' names to replace NaN
df.dropna(subset=['Questions'], inplace=True) # remove rows with no questions/answers
table = pd.pivot_table(df, values='Answers', index='Students', columns='Questions', aggfunc=np.mean)

table.to_csv('C:/Users/username/Desktop/survey-pivoted.csv')
