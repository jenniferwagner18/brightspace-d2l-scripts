# Brightspace by D2L Scripts

These Python scripts clean and format data in reports downloaded from Brightspace by D2L or Insights Report Builder.

## Intelligent Agent
Merges the exported classlist CSV and the export history CSV of an intelligent agent from D2L. The export history does not include usernames or email addresses, while the classlist export only can include usernames and/or email addresses (if enabled by admins). If only usernames are included, this script formats the email addresses properly, including if guest accounts with various domains are used. Output columns are Last name, First name, Email address, and if the user was identified in the intelligent agent (True or False).

Excel workbooks for adding usernames/email addresses to an intelligent agent export history are also available using [formulas](https://github.com/jenniferwagner18/brightspace-d2l-scripts/blob/main/d2l-intelligent-agent.xlsx) or [Power Query](https://github.com/jenniferwagner18/brightspace-d2l-scripts/blob/main/d2l-intelligent-agents-power-query.xlsx).

The manual way of joining intelligent agents and the class roster using Power Query in Excel is shown in [this Intelligent Agents video](https://mediaspace.msu.edu/media/1_cdn8k42f).

## Outcomes Pivot
Pivots the data in a learning outcomes data set generated in Insights Report Builder so that it matches the Mastery View table in D2L. Students are in rows, outcomes are in columns, and the mastery levels are the values. The [data flow](https://github.com/jenniferwagner18/brightspace-etl-dataflows/blob/main/mastery-view.md) for generating the outcomes CSV file is available from the brightspace-etl-dataflows repository.

The manual way of creating the text-only pivot table in Excel is shown in [this Outcomes data video](https://mediaspace.msu.edu/media/D2L+Outcomes+Data+PivotTable+to+re-create+Mastery+View/1_2f4z3wn3).

## Survey Pivot
Pivots the data in a Survey report (individual attempts) of Likert questions downloaded from D2L so that the questions are in columns instead of in rows. If there are multiple attempts on the survey, the responses are averaged.

The manual way of cleaning the data and creating the pivot table in Excel is shown in [this Survey Report video](https://mediaspace.msu.edu/media/D2L+Survey+Report+PivotTable/1_jyh0yyk8).
