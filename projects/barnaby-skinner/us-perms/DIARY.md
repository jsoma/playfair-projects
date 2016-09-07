# Exploring the data

1. Joining all the data sets.

2. Creating the dummy variables to then make the predictor, and to create the map.

3. For some reason the join with the .shp file in pandas doesn't work, or both
Carto and QGis don't read the merged columns. So I repeated the join in Carto.

4. I struggled to find any correlation between the wage and the acceptance.

5. I decided to work out the acceptance rate of the various nationalities,
and plot that out. Maybe map it out at a later point.

6. I am working with the SOC codes to define the professions of the applicants.
Turns out they are very difficult to cluster, because the

#Reading on PERM data

1. [PERM Visas](https://www.usavisanow.com/perm/)
2. [More on PERM Visas](http://www.usa-immigrationlaws.com/legal-services/employment-visas-p-e-r-m)
3. [Query Service](http://redbus2us.com/green-card-sponsors/index.php?searchText=microsoft&searchYear=05&action=search&pn=2)

#Sources for map
[Natural Earth Data](http://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/)
[SOC Codes](https://docs.google.com/a/tamedia.com/spreadsheets/d/1SGhlKSD8ZaFDSKkJeStUfA6amumiQvs4aPfFgoCfaC4/edit?usp=sharing) my manipulated data
[SOC Codes][http://www.bls.gov/soc/]

#Getting it to tun on Heroku
1. Installing Scikitlearn on Heroku is a little bit of a problem. This helped, however:
https://github.com/thenovices/heroku-buildpack-scipy
2. Next steps will be woring with Pickle to store the model and SQL to possibly query data.
We'll see.
