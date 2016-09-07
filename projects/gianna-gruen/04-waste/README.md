**Line graph: Waste generation over time by country**
Data source: [OECD](https://data.oecd.org/waste/municipal-waste.htm)

- cleaning data
- parsing time
- subplotting each countries time series in one graph
- exporting to illustrator, annotating manually

**Scatter plot: Packaging waste generation vs recycling (per capita)**
Data source: [Eurostat: env_waspac](appsso.eurostat.ec.europa.eu/nui/show.do)

Select:
* all packaging waste per capita
* all recycling per capita
* 2013
* kg per capita

- scattering total amount of waste generated against total amount of waste recycled yielded in a perfectly correlated graph
- to differentiate, breaking the data down in several waste-types


**Hazardous waste**
Data Source [Eurostat: env_wasgen](http://ec.europa.eu/eurostat/web/waste/generation-of-hazardous-waste-by-economic-activity)

Select:
* all hazardous waste (plus subset: chemicals and minerals)
* total amount in tonnes
* 2012 (latest available)

For total amount of hazardous waste, chemical hazardous waste and mineral hazardous waste
- Data cleaning in pandas
- Exporting cleaned data using `selection_haz.to_csv('hazardous_waste.csv')`
- Importing cleaned data into carto
- Make carto recognize the GEO-strings as geocode information by: Edit > Georeference > Admin.Regions > Select region: set to geo column > choropleth map
As maps for all three resulted in same clusters of countries, I only continued with total hazardous waste amount

- xport as shp file
- opening in qgis, adjusting projection, color range and setting boundaries to Quantiles
- changing boundaries to some nicer numbers without changing actual clusters of countries
