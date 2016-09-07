# BOTica analysis: The 8 most wanted medicines.

For this chart I used data collected by a Twitter BOT. The BOT's name is BOTica and it is basically a platform for Venezuelan users to request and donate medicines. I came up with this idea while thinking of ways to help with the health crisis that my country is currently facing.
I plan to do charts like this one every 2 weeks to drive attention to what is needed the most and make the donation process easier for the donor (the chart's legend tells the donor what user is asking for each medicine).

### Data Source
I manually created a data set from info collected by BOTica. I've uploaded the csv file with the rest of the documentation.


### What I wanted from the data:
There are many things I could do with the data collected by BOTica. I decided that since I don't have a big dataset yet I was going to use what I had so far to help grow the project. Once I receive more requests for medicines I can do a broader analysis and analyse information such as, what are the cities where most people are donating/requesting medicines, how frequently does BOTica receive a Tweet, how many matches has BOTica made between donor/person in need, etc.
So what I wanted from the data was to see what medicines users where asking for, and help find donors. A donor might not scroll through the whole feed looking to see if someone is aking for a medicine she/he has. So if I create a chart with a quick summary of what people are asking for, maybe more donors would be attracted to donate.
And that's what I did, I took all of the medicines that had more than 1 request and created a chart. The y axis takes the names of the medicines, while the x shows the number of users asking for them. I created a legend with the twitter handles of all users asking for each medicine.
 
  
### How I worked with the data and what problems I encountered
I used Twython to get all tweets by BOTica (the BOT receives DM from users and tweets them). 
I also used TextBlob to analyze the text in each Tweet by BOTica and find the most common words (look at ipython notebook for process). From there, I filtered to keep only the names of medicines.
The text in each tweet was different so I had to do a specific analysis to each tweet despite the fact that I could get every word in all of them (more info in DIARY.dm). Then I manually created an excel file with the name of the medicine and the Twitter user requesting it or donating it.



