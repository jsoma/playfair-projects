## How accessible is Madrid's subway network?

The first issue I encountered when starting this project was the lack of data in an electronically accessible format. [Madrid subway's website] (https://www.metromadrid.es/es/viaja_en_metro/red_de_metro/estaciones/index.html) had detailed information about its 275 stations, but scraping was needed. When trying to do so, I found out that they were blocking these kind of method. I therefore had to build my database manua
For each station, I have stated - based on the information Metro de Madrid publishes - whether it is adapted for people with disabilities, it is equipped with elevator and/or escalators, or just stairs. Since several stations connect more than one line, I have created four columns ('Línea 1', 'Línea 2', 'Línea 3', 'Línea 4') to store the value for each one without adding more than one row per station.

Yet I needed some additional information about when had the stations been inaugurated or revamped, so I asked Metro de Madrid's press office for it. Since this proved impossible (apparently, it is a huge task to get this data from all the stations in the network), I lowered my demands and I asked for just the inauguration and/or last revamp date for every line (15). I also wanted to know what does "adapted for people with disabilities" mean (that is, which criteria must a station meet to be considered into this category). Two weeks later, I am still waiting for the information (being in the middle of the summer does not help). UPDATE: I just got all the information I needed (only in a scanned PDF!!!). I Have built a new database based on that information, with the inauguration date of each line or enlargement.

After receiving some feedback from fellow students, I have also looked for data regarding the number of passengers per line, to check whether the most used lines are also the less accessible. Again, [Metro de Madrid's website] (https://www.metromadrid.es/export/sites/metro/comun/Portal_de_transparencia/Documentos/Informacion_economica/Demanda_2015.pdf) is my source.

I have already carried out some analysis on my database. Here are some of **my main findings**:

* Two thirds of the stations (183, 67%) are adapted for people with disabilities.
* In more than half the stations (157, 57%) there is an elevator.
* Three in four stations are equipped with escalators (202, 73%).
* More than half of all the stations (146, 53%) do have both escalators and an elevator.
* 12% of the stations (34) have neither elevator nor escalators. 11 of these (the highest number) belong to Line 1, the oldest, which is undergoing major construction works this summer. However, as Metro de Madrid press office has explained to me, this repairs do not include revamping the stations. That is, there will be not improvement to make them more easily accessible for people with mobility problems.

### Viz

I have created three different maps (based on the one available at https://www.metromadrid.es/export/sites/metro/comun/documentos/planos/Planoesquematicoespanol.pdf):

* A general map, including all the stations in the network (regardless of their level of accessibility)
* A zoomed-in map of the stations in central Madrid
* A map of only those stations that are fully accessible

I have also added a fourth one (based on the one available here: https://www.metromadrid.es/export/sites/metro/comun/documentos/planos/PlanoMetroTurInterior.pdf), which shows Madrid's main touristic sightseeings and the nearest metro stations.

When trying to add other kind of graphs (like bar charts), I have realized that I need to turn the columns grading the accessibility (now based on a Yes/No value) to binary values (1=Yes, 0=No). I am having problems with turning my database into a bar chart, because of its structure. I have finally fund out that there is possibility to create pivot tables in pandas, so I have created one representing the % of stations for each degree of accessibility (just what I wanted to visualize!!).

Working on my graph, I have tried to create a small multiples chart. I have had a lot problems when writing the code, since I have more than one variable. One of them has been positioning the bars where I wanted them to be (not really convinced of the final outcome, I would have wanted them to be one by each other and not separated). Another challenge has been labeling the charts in Python (just could not, so I'll try to do it in Illustrator).

I finally abandoned the idea of the small multiples and stuck to the original bar chart (even if I am not convinced at all about how it looks).
