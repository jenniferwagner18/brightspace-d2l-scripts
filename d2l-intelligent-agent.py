# This script merges the classlist exported from D2L gradebook with the export history of an intelligent
# agent and formats the email addresses properly even if guest accounts with various domains are used.

# Don't forget to replace @yourschool.edu with your institution's domain.

import pandas as pd
df1 = pd.read_csv('classlist.csv')
df1.columns = df1.columns.str.replace(' ', '')
df2 = pd.read_csv('agent.csv')
df = pd.merge(df1,df2,on=['LastName', 'FirstName'], how='left')
df = df.drop_duplicates(subset=['Email'])

df['Identified'] = df['AgentName'].notnull()
df['Email'].replace(r'_at_', '@', regex=True, inplace=True)
df['Email'] = df['Email'].where(df['Email'].str.contains('@'), df['Email'].astype(str) + '@yourschool.edu')

df.to_csv('agent-final.csv', columns=['LastName', 'FirstName', 'Email', 'Identified'], index=False)
