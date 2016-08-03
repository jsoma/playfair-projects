# Diary of Map the Fans

- The import of the data was straight forward. 

- Since ZIP codes can not be clearly assigned to one community, I need to remove the column with the name of the community. Probably, I will reimport it later with the Shapefiles of the ZIP code areas. This sorce seems to be more reliable. 
- The data from SCB contained a number of rows for the same ZIP code. I grouped it, so that I have just one row per ZIP code area.
- It took me quite a while to merge the three different datasets. 
- I tried to find correlations between the number of season cards and socia-demographic information. Since the values in the socio-demographic data are evenly distributed, I couldn't find any usable correlation.
- I did analyze the number of cards for both clubs and the number per capita. I finally made some plots. 

### Mapping part 

- I am generating a csv file of the necessary information out of Pandas. 
- The import of this file into 
- I was also trying to do that directly in javascript using the [Leaflet Library](http://leaflet.org). I could generate a map. To get it to work, I had to simplify the shapefile with [Ogr2](http://gdal.org/ogr2ogr.html). But still with a strong generalization the map reacted slow. Therefor I decided to stick with 'Carto'. 
- The colors in Carto are hard to adjust. It doesn't look pleasant that the areas without data are covered by yellow or white too. I would rather like to see more of the main map. 
- If you're changing back to the wizard of Carto, you will loose all your adaptions in the HTML and CSS code. Not nice...
- Importing the data to Carto. Finally importing the shapes of the ZIP areas, too. Merging the two tables. 
- I finally had to get information about the community name for each ZIP code. They are ambigous. I inserted the most important name.
- Because of my lack of javascript knowledge, I couldn't get a nice selector to display the maps to work. The TA and I were trying for an hour...
- I finally managed putting the maps together using [iframe scaffolder](http://pirhoo.github.io/iframe-scaffolder/). And with a little help from Paul I finally got the own html and javascript code to run. 
- I would love to generate maps directly from Pandas. I was trying to do this, but didn't suceed because I couldn't find all the necessary libraries.
- I finally exported some PNGs of the maps. 


