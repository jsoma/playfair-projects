# Spanish female athletes
## Scraping ADO's website
### This part of the project would have been impossible without the help of @nickyforster

The information I needed for this project is available [here](http://www.coe.es/ADO/ado09.nsf/de000d1322082c17c1257ddc005a8d36?SearchView&Query=(2016)&Start=1&Count=171&SearchOrder=4). 'Available' is a nice way to put it. Although the list of the athletes is apparently part of the same page as the rest of elements, the truth is harder than that: the main frame for the site is a WordPress template and the list of athletes is embedded within it. Besides, the first list only includes basic information about the athletes. All that has to do with the competitions they have taken part in and their classification is buried in another page, with its individual URL per each athlete.

So first of all I needed to scrape the list of all the sportspeople and their unique URL's. That seemed easy. But again reality was harder. The name, sport, birthplace and URL of each individual was included within a <td> tag, but there were no unique classes attached to those tags. So I had five 'keys' and their 'values', but I needed to link each key to each value. Nicky came out with a solution that you can see in the iPython notebook attached to this project.

Then I realised that the gender information (key to what my project was trying to show) was not there. I had to add it manually, creating a list with the names of the sportspeople, converting it to a .csv, adding the info and feeding it back to pandas as a dataframe. Since it was to be merged with the first athletes' list, it had to be a list as well (check the iPython notebook for more info on that, it took a couple of additional steps). After some attempts, I finally merged the two lists into oe, thanks to some code I found [here](https://mmxgroup.net/2012/04/12/merging-python-list-of-dictionaries-based-on-specific-key/). What was important about this code is that it allowed me to merge both lists, but it also deleted the information ('name') that was redundant after the merge.

After building a scraper for the corresponding HTML tags and zipping two sublists, I already have the 'players_list', where I am storing the keys and values with the basic info for each athlete.

Next step: adding the headers of each athlete's competitions to the main `for` loop. After several hours struggling with the problem I finally figured out why the zip solution that I used for the athletes' basic info does not work here: in the former case, there were five keys and five values. In the latter, however, this is not the case, since there are more elements to be taken into account: just like in the previous case, on one hand, there are the headers (5), which act as keys; on the other hand, there are the results (5), which act as values. The problem is that the headers/keys are stable, while the results/values vary in number. When using a `for` loop, I am forcing the scraper to try to gather the 5 values (one per key) 5 times, since there are 5 elements in the zipped list.

I am trying to find a way to merge to lists of different length. Not easy, it seems.

In the end, I just added the headers manually (including the athlete's name to be able to keep track of which results belong to which player), and solve a couple of problems with none types appearing at some points in my database. Then I created just three lists of dictionaries: one for the athletes' info, another for their results and then a final one for the info about the years when each athlete has received public funding. After that, I have merged the list with the athletes' info and the one with the results, and then created a dataframe. I had to clean it a little bit to turn the classification string into an integer.

For plotting the data, I created sub-dataframes for each competition. I am working on bar charts, so far.

Just finished polishing the first bar charts with Inkscape (amazing tool, btw). For the moment, they only focus on the number of medals won per gender per competition and in total. Now I would like to go deeper in my analysis and see what I find. I think my database can provide a lot of insights.


I wanted to do a chronological analysis, but I did not have time data. The only reference to a year is was contained in the names of the meetings or competitions They were easy to strip form the Olympic Games, since they always follow the same structure, but it was a nightmare for the World and European Championships. So I have added them manually, and then I have merged this data with the original data frame where all the information for the athletes was.

I have created a sub-data frame to analyze just the top classifications (gold to bronze medals). Since my information about the gender is stored under the same column with two different values, in order to analyze the performance of both genders over time, I had to split the data in two new sub-data frames to see the evolution of both genders separately. I am planning to plot these as line graphs.

The year data is not working when it comes to plotting. I have quit that idea.

I have finally decided to make a series of graphics to present all the information in a broadsheet.

I also have added a scatterplot in d3.
