# Diary

- This project was quite ambitious for the short time. First, I had to write the webscrapers. Then I had to wrangle the data and finally analyze the data. 
- It took me a long time to write the webscrapers. While the first two were quite straight forward, I was struggling with the third and the forth one. 
- We couldn't find the necessary information in the source code. Finally, we discovered that it was delivered as JSON file. After it was quite easy to write the necessary code. 
- The last website, the one from MeteoSchweiz, does provide the data in JSON format too. I did struggle with the timestamps. They were first looking like UNIX timestamps but did have too many characters. Finally I figured out: I just have to drop the last three numbers (always zeros). Probably, these were the milliseconds.  
- The next approach to get the data from the website of MeteoSchweiz did fail. The reason: The name of the file did change. There are somehow the minutes encoded in the name of the file. But at what minute are the JSOM files generated? I did try to discover the pattern in the file name, but didn't suceed. The last part differs between the different files json files. I thought a couple of times that I found it. But the next day, I got mail from my baby server...
- Didn't find a way to resample my data from SMN to hourly values yet.
- Struggling with timezone aware and unaware timestamps took a lot of time... I finally adapted the values in the raw data and changed the scraper.
- The scraper needs more changes. And I need to program additional scrapers, so that I will get the most comparable values.
- After a long struggle we found out: The problem with resampling a timeseries is not a problem of resampling -- but of a missing font in the stylesheets. 
- Still struggling with timezone aware and naive times. They are not compatible. 
- After an hour of trying, the TA and I found a solution for the timezone issue. Let's make all times -- kind of -- timezone aware instead of trying to get rid of the timezone information in one dataframe. 
- I learned the hard way that df_new = df is not the same as df_new = df.copy(). 
- Trying to put all together. Made the first graph.  
- Added brute force to one of the scrapers: Since the filename differs in one number, I am trying up to 20 possibilities. The scraper will just be running once daily and I implemented a delay, so this shouldn't cause any problems. 
- Two provider didn't show up on the graphic. I didn't figuring out why for a long time. The TA and I finally found a solution: We need to drop the NaN values before ploting.  
- I tried to generate the graphs headless on my baby server, but didn't suceed yet. 
