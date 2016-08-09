## Accessibility of Paris' subway network

I had to change the extension of the Excel file, since it seemed to be originally a .xml that Pandas could not read. Turning it into a .xls file solved the problem.

Based on the documentation that the RATP has sent to me, I know that the column that indicates whether an station is accessible or not is the one called "Accessibilité UFR" (*"accessible for people on a wheelchair"*). There are other four indicators regarding the visually and the hearing impaired. I plan to use this later. In all these columns, the information is encoded as "0" for non-accessible and "1" for accessible.

After a first rough analysis, I found out that 83% of the stations in Paris' subway are not accessible.

There seems to be geographical information about where the stations are located, through the department number. However, this only tells us whether the stop is in Paris or in the outskirts of the city.

According to the documentation, the "Stif" code is the identifier for the line, so I have grouped the stations based on this criterium. The codes are quite arcane. Looking into data available [here](http://opendata.stif.info/explore/dataset/referentiel-des-lignes-stif/), I have been able to match each code with the name of the line, except for code 1001110020001. Taking a look at this four stations to check their names and doing some research, I have found out that they belong to line RER B. So now I have the real names of the lines.

I have plotted the data in a very simple bar chart, which I will polish in the coming days. This dataset has made me realize the importance of using binary classes for categorical data when building my own databases.

I have realized that I was plotting the % of non-accessible stations, when what I really want is the opposite (this is what I have visualized in my project about Madrid), so I need to create a new dataframe based on the accessible stations. The process of creating the df's fro the plotting has been time consuming, since I needed to group the accessible stations per line and then the total stations per line, and then merge it all into one, so that I could do the math on it.

Once the bar chart is polished in Python, I have finished it in Illustrator. I needed to do a little more research on the commercial names of the rest of lines, so that I could "translate" the "Stif" code the RATP uses.

After receiving my peers' feedback, I have changed my idea of the graph and combined three bar charts with information about the % of accessible stations per line for Madrid, Paris and NYC, all under the same title and introductory paragraph.

Just another change: after someone suggested using stacked bars, I am going for it!
