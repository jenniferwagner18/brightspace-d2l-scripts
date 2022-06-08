# Brightspace by D2L Scripts

These Python scripts clean and format data in reports downloaded from Brightspace by D2L.

## Intelligent Agents
Merges the exported classlist CSV and the export history CSV of an intelligent agent. The export history does not include usernames or email addresses, while the classlist export only includes usernames. This script formats the email addresses properly, including if guest accounts with various domains are used. Output columns are Last name, First name, Email address, and if the user was identified in the intelligent agent (True or False).

An [Excel spreadsheet](https://github.com/jenniferwagner18/brightspace-d2l-scripts/blob/main/d2l-intelligent-agent.xlsx) for adding usernames to an intelligent agent export history is also available.

## Survey Reports - Individual Attempts
Pivots the data in a Survey report (individual attempts) of Likert questions so that the questions are in columns instead of in rows. If there are multiple attempts on the survey, the responses are averaged.

The manual way of cleaning the data and creating the pivot table in Excel is shown in [this video](https://mediaspace.msu.edu/media/D2L+Survey+Report+PivotTable/1_jyh0yyk8).
