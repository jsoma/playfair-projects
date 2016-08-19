Data Source:
[NYPD, 2015](http://www.nyc.gov/html/nypd/html/analysis_and_planning/stop_question_and_frisk_report.shtml)

To get a general understanding of the dataset, I first looked at the most recent data of 2015 -- to see which variables to investigate and what might be interesting for further analysis.

I decided to go with
1. The total number of stops per year
2. A racial breakdown of these numbers
3. Per race, showing how many people were also frisked.

I got the yearly csv files from the NYPD (see data source link above).

For **1 and 2** I looped through each data set, assigning the year and the total number of entries in each dataset to a dictionary and appended that dictionary to a list (gathering data for 1).

In the same loop, I did a value.counts() for the 'race' column and turned it into a df, merging each new df to the previous one (gathering data for 2).

Last step was to add the df from 1 to the df produced for 2.

**1: Time Series**
Taking the list of dicts, converting the year into a datetime object and plotting it.

**2: Racial Breakdown**
Because data gathering for some races was inconsistent over time and also for enhancing the narrative, I ignored all data but that for black, hispanic and white people.

To get the total of all others, I added black, white and hispanic up and subtracted the sum of the total count gathered for each year.

Did a stacked bar chart of black, hispanic, white and all others, using [this code from Chris Albon's website](http://chrisalbon.com/python/matplotlib_percentage_stacked_bar_plot.html).

**3: Frisked Share**
Only taking 2015 data, creating a frisked vs non-frisked breakdown for each of the three selected races.

Adjusting the size of each pie chart to the total number of people of this race being stopped. Black people with the highest number set to 100%, others adjusted in relation to it. 
