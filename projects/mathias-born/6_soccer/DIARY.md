# Diary

- In this project I try to clean up and work with data gathered from the sports department of my newspaper. Since the work on the data is not finished yet, I will just publish an excerpt. 
- The data is collected in a Google spreadsheet. The format might be useful for the guys filling the information in -- but not to work with the data. In a first step I had to completly reorganize the data. Since the people in the sports department will add new transfers, I wanted to be able to reproduce all steps as quickly as possible. Therefore I decided to do it in Pandas. That took quite a while...
- Finally, I can query the data if needed. 
- There are problems with the geo coordinates. I might want to include the exact coordinates of stadiums later. I just [found a list here](http://opisthokonta.net/?p=619). 
- I spent a couple of hours wrangling with the date format. The date seems to be an integer (with two decimal points...). I tried to change it to a string. But parse from dateutil didn't like it. It said: Unknown string format. After hundreds of experiments and a lot of googling, I found the solution: pd.to_datetime(df_bis, dayfirst=True, errors='coerce'). Probably there are some errors in the dataset somewhere. I just ignore these for now.
I spent most of my evening trying to figure out how to apply a regular expression... There's a problem with the data: The names of the town are not consistent. 
- Unfortunately, there are now duplicates in the dataframe. Problably they are generated while creating the index. For now, I am just droping them. But I will need to take a closer look at this problem.
- I am calculating the difference between two dates. Since the field contains now not only the number but also 'days', I can't plot the number. I tried to convert it to a integer. Since I didn't suceed after trying for a long time, I decided to convert it to a string and then use regular expressions. 

