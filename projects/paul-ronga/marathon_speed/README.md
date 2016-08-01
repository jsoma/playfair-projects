# How marathon runners run

The marathon “La course de l'Escalade” is a race which takes place each year in December in Geneva.

It has more than 30 categories. My first idea was to plot the age (x axis) and the time (y axis) of all runners to give a glance at these categories.

This resulted in a huge, ugly scatter plot which didn't help at all. Actually many categories have a different path length, so a time comparison doesn't make sense.

Then I chose to draw two visualizations: 

* a graph about the two categories which group athletes and confirmed runners (Escaladélite);

* a small multiple containing the 8 first categories of runners.

I eventually realized this second visualization doesn't bring much and add noise to the information brought by the first one. You can still find its draft [here](https://cloud.githubusercontent.com/assets/12730304/17273556/d407ec18-5686-11e6-87a9-be3e6cfa6baa.png), but it's not part of the story anymore.

Age has no linear correlation with performance. The r value is -0.428099. The fastest female runner is 21, but the second one is 33. The second fastest male runner is 32.

We notice the speed can vary almost twofold. The fastest people run at near 21 km/h, the slowest (in the Elite categories) at 11 km/h.

The median age, for elite runners, is 35 (m) and 34 (f).

## Data set

Here's the data:

[Data_selection.csv (preview)](https://github.com/palrogg/playfair-projects/blob/master/projects/paul-ronga/marathon_speed/Data_selection.csv)

[Data_selection.csv (raw)](https://github.com/palrogg/playfair-projects/raw/master/projects/paul-ronga/marathon_speed/Data_selection.csv)