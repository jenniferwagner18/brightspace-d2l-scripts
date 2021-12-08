# Brightspace by D2L Scripts

These Python scripts clean and format data in reports downloaded from Brightspace by D2L.

## Intelligent Agents - Earned Award
Merges the exported classlist and the export history of an intelligent agent based on release condition of earning an award. The export history does not include usernames or email addresses, while the classlist export only includes usernames. This script formats the email addresses properly, including if guest accounts with various domains are used. Output columns are Last name, First name, Email address, and if the award was earned (True or False).

## Survey Reports - Individual Attempts
Pivots the data in a Survey report (individual attempts) of Likert questions so that the questions are in columns instead of in rows. If there are multiple attempts on the survey, the responses are averaged.

The manual way of cleaning the data and creating the pivot table in Excel is shown in [this video](https://mediaspace.msu.edu/media/D2L+Survey+Report+PivotTable/1_jyh0yyk8).
