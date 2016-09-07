My story was originally tentatively going to be called "Dead Trees in East New York", because I noticed that as far as value counts, ENY has way more dead trees than any of the other neighborhoods, in this case grouped as "Neighborhood Tabulation Areas". It's what NYC uses in the census, and mostly lines up with neighborhoods.

The data I used is here:
https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh

I set about trying to figure out just how many dead trees vs. alive trees there are, but this was difficult. It took me a while to find a way to turn a discrete column into percentages of dead trees. I finally accomplished that by using a for loop to count the length of slices of my data frame and output that into a csv that I could then manipulate.
