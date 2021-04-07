This project aims to calculate some statistics for byke share usage pattern. We have data for 3 major cities: Chicago, New York City and Washington. 
The user can select a certain city to get its data summaries, then he can filter its data by month and/or day if he wishes. He can select "all" if he doesn't want to apply filters. He must enter full month/day names to filter with.
Then the system calculates and shows statistics for the selected data, and then asks the user if he wants to view a sample of data. The system shows a sample of raw data as long as the user replies with "yes"
The system asks the user if he wants to restart, then the whole process is restarted if the user answers with "yes", otherwise it exits.

Resources:
https://stackoverflow.com/questions
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.copy.html
https://www.geeksforgeeks.org/python-pandas-dataframe-sample/
https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html
