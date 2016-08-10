#"Voter Turnout: U.S voter turnout notoriously low compared to other developed and emerging economies"
# Story: The U.S has a very low voter turnout. I wanted to explore how other countries do, and why or how they are doing better than the U.S in this aspect.

I had the idea to work on this subject when I read this article by the Pew Research (http://www.pewresearch.org/fact-tank/2016/08/02/u-s-voter-turnout-trails-most-developed-countries/).
My original idea was to recreate the map on the article but as I did some research I decided to add to additional charts to help tell a bigger story.

## Possible questions to ask the data:

  - What is the voter turnout rate for the U.S?
  - How does this rate look compared to other countries?
  - Why is the rate so low?
  - What are the countries with the highest or higher rate that the U.S doing differently?


## Problems I encountered

#First chart
-The dataset for this chart was clean so I did not have problems working with it. I was missing a piece of information, which was the percentage of voting age population that voted in the most recent elections in Australia, so I did some research and was able to add that to the dataset.
I also had one question about the data itself and it was that for some countries the percentage of registered voters was less than the percentage of voting age population. Pew Research specifies in its article that this is the case for a number of countries. 
I wanted to know the explanation behind it and contacted Pew Research.
I did not hear back from them but my own thinking tells me that this is possible since we are using the percentage of voting age population (how many people old enough to vote cast a vote) and the percentage of registered voters(the number of registered voters that actually cast a vote).
This would not make sense if we were saying that the total percentage of registered voters is more than the total percentage of voting age population because that is IMPOSIBLE.
-I encounter a problem when trying to plot the data using a scatterplot. I had planned to use the country names as my Y- axis and the % of voter turnout for my X-axis. 
The problem was that python could not plot a scatter plot with non numerical information for the Y-axis. So I had to use my index as the Y-Axis (that way I had a number to country relationship so I could later edit it using illustrator).
I imported the chart to illustrator and manually changed each number for the corresponding country. I also had to move my grids around since I wanted each country to have its own row in the chart and what I had was one country per line, which looked very messy.

#Second chart
-For this chart I needed to include both the data for voter turnout and the information for whether the country had compulsory voting laws.
I first tried to integrate everything in the same chart but my peers told me it was too confusing. I decided to make a chart and accompanying with a explanatory table.

#Third chart
-The third chart was the easiest. However, my original idea was to use voter turnout rates data and also information of the percentage of the voting eligible population that is registered to vote (not the percentage of the registered voters that actually voted). 
The difference might be dismissed but it is a very important one, for example, in 2012, there was an 84.3% voter-turnout of registered voters in the U.S. But only about 65% of the voting-age population was registered to vote. 
By doing that we would compare how many registered voters there are in each country, whether registration is universal or not, and how that reflects in the voter turnout.

## Design decisions
  - At first I was not sure if it was a good idea to mix different types of charts for the same story. I thought my opening chart (scatterplot) was a bit hard to understand and it would confuse my readers to suddenly change to a bar chart format.
  However, my peers disagree and said it was a good idea to use different formats to tell the different parts of the story.
  -I used font size and type to give hierarchy to my story since it had so many elements.
  -When I first put the 3 charts together it looked messy. I tried using a light gray background for each of them and it helped a lot with the look.
  