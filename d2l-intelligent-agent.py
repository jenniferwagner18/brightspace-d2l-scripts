# This script merges the classlist exported from D2L gradebook with the export history of an intelligent
# agent and formats the email addresses properly even if guest accounts with various domains are used.

# Replace @yourschool.edu with your institution's domain.

import pandas as pd
df1 = pd.read_csv('classlist.csv')
df1.columns = df1.columns.str.replace(' ', '')
df2 = pd.read_csv('agent.csv')
df = pd.merge(df1,df2,on=['LastName', 'FirstName'], how='left')
df = df.drop_duplicates(subset=['Email'])
df.rename(columns={'AgentName': 'InAgentReport'}, inplace=True)

df['InAgentReport'].replace(r'^.+$', 'True', regex=True, inplace=True)
df['InAgentReport'].fillna('False', inplace=True)

df['Email'].replace(r'_at_', '@', regex=True, inplace=True)
df['Email'] = df['Email'].where(df['Email'].str.contains('@'), df['Email'].astype(str) + '@yourschool.edu')

df.to_csv('awards-earned.csv', columns=['LastName', 'FirstName', 'Email', 'InAgentReport'], index=False)
