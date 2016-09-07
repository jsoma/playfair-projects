## Design choices
* **Font** Raleway Family
  * Header: Heavy Black, 34 pt
  * Descriptive Text: Light, 16 pt
  * Axis Labels: Regular, 12 pt
  * Annotation: Regular, 10 pt
  * Source: Regular, 10 pt
* **Color**:
  * Purple Navy: #404e7c
  * Sunset Orange: #fe5f55
  * Turquoise: #4ce0d2
  * Sandstorm: #e8d245
  * Soap: #c6caed
  * Fall back for Soap: Silver Sand: #c2c1c2

## Project 1: Energy transition
Germany is hyped for its energy transition: the aim to meet 80% of its energy demand with renewables and cut primary energy demand by 50%, both by 2050.
Moreover, by 2022 the government wants to abandon nuclear energy. Countries like Japan, the US and Britain look at Germany's progress and there's the general perception of 'If the Germans can make it, we can, too!'

However if you look at other European countries, Germany is not leading the *Top10 in Renewable Energy* , but countries like Norway and Sweden are doing way better. Already now the exceed by far the goal the EU set: 20% of energy consumption from renewables by 2020 and use 80% and 50% renewable energy, respectively. Why  aren't they the role models?

Idea for graphic series: Shed light on how European countries compare on renewable energy production and to see whether Germany is or is not a good role model

#### Questions:
* What is each countries total energy demand? (total)

* What is household energy consumption? (per capita + share of total)

* How do countries compare in renewables vs non-renewables as energy source?
[two sided bar graph]

* How has usage of renewables changed over time? (compare 2000 and latest data)
[slope graph]

* How has the energy price changed over time?

* How does energy production distribute over energy sources?
[multiples?]

* Does energy demand relate to GDP and use of renewable energy? (maybe include non-EU-countries)
[scatterplot, x = GDP, y = energy demand, bubble size = share of renewable energy in energy mix]

* How does energy production/use relate to subsidies? (select 5-10 interesting countries based on previous analysis)
[colored scatterplot, one color per energy source, one markertype per country]

#### Headlines:
* For a role model on renewables, look at Norway, not Germany
* The difference that you NOT make -- why saving energy per household doesn't matter
* Discover the hidden champions of energy transition

#### Data Sources:
* [EU data -- renewable shares](http://ec.europa.eu/eurostat/statistics-explained/index.php/Renewable_energy_statistics)

* [EU data -- energy consumption](http://ec.europa.eu/eurostat/statistics-explained/index.php/Consumption_of_energy)

* [EU data -- fossil + nuclear -- EU total](http://ec.europa.eu/eurostat/statistics-explained/index.php/Electricity_production,_consumption_and_market_overview)

* [EU data -- fossil + nuclear -- EU by country](http://ec.europa.eu/eurostat/statistics-explained/index.php/Energy_production_and_imports)

* [EU data -- subsidies](https://ec.europa.eu/energy/sites/ener/files/documents/ECOFYS%202014%20Subsidies%20and%20costs%20of%20EU%20energy_11_Nov.pdf)
[Annex2](http://ec.europa.eu/energy/sites/ener/files/documents/DESNL14583%20Final%20report%20annexes%201-3%2011%20Nov.pdf)
[Annex4](http://ec.europa.eu/energy/sites/ener/files/documents/DESNL14583%20Final%20report%20annexes%204%205%20v3.pdf)

* [EU data -- energy price](http://ec.europa.eu/eurostat/statistics-explained/index.php/Energy_price_statistics)

* [EU data -- comparison to world](http://ec.europa.eu/eurostat/statistics-explained/index.php/The_EU_in_the_world_-_energy)

* [Energy by country](http://ec.europa.eu/energy/en/data-analysis/country)

* [International Data -- pick three for comparison?](https://data.oecd.org/energy/renewable-energy.htm)

#### Further links:
* [Renewables 2050: Global Status Report](http://www.ren21.net/wp-content/uploads/2015/07/REN12-GSR2015_Onlinebook_low1.pdf)

* [Subsidies and cost of EU energy, p.8](https://ec.europa.eu/energy/sites/ener/files/documents/ECOFYS%202014%20Subsidies%20and%20costs%20of%20EU%20energy_11_Nov.pdf)

* [Energy taxation and subsidies in the EU and Norway](http://www.nera.com/content/dam/nera/publications/archive2/PUB_OGP_0514.pdf)

* [Carbon Brief: Europe's progress on renewable energy in five charts](https://www.carbonbrief.org/five-charts-showing-the-eus-surprising-progress-on-renewable-energy)

* [Carbon Brief: Five weird things about the cost of energy study](https://www.carbonbrief.org/five-weird-things-about-the-eus-cost-of-energy-study)

## CURRENT STATUS AFTER PEER FEEDBACK

### Focus on fewer questions:
- renewable vs non-renewable (absolute? share! -- two sided bar graph)
- renewable use related to price? (scatter? two lines?)
- (GDP or population) linked to energy consumption linked to (renewable or renewable subsidies)? (scatter w/ varying bubble size)

### Process & problems
* **Problem: Sourcing data**: Eurostat has tables as jpgs (!) on it's site and instead of linking to the excel file, you are redirected to the database containing the information.
**Solution**: Reconstruct the dataset by imitating their query, download giant dataset, filter for the energy unit desired, year desired, columns desired.
http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=nrg_100a&lang=en
nrg_100a

* **Problem: Data Formatting** data comes in 1,234.5 format -- Python doesn't recognize the , so 234.5 will be bigger than the previously named figure.
**Solution** list comprehension to replace , with nothing: `[float(value.replace(',', '')) for value in selection_t_c['Value']]`

* **Problem: Old columns with unformatted data and same column titles**: As I would want to merge some df at some point I needed to get rid of old columns with same names to make things less confusing.
**Solution:** `df = df.drop('column_name', 1)`

* **Problem: Look at production or consumption?** First I looked at energy production, because I thought that would be a good variable. I was interested how big the renewable share in overall production is. However, for some countries that is 100% (Cyprus, Malta, Latvia...). So I thought it might be more insightful to look at consumption instead. So I repeated all analysis from before, just filtering for 'gross inland consumption' this time instead of 'primary energy production'. Calculating the share of renewables in total energy consumed led to pretty high values, with Norway being an extreme outlier: the country consumes 6 times more energy than it overall consumes. I cannot think of a scenario that makes this plausible.
**Ideas to tackle**:
- check a third time whether there's no data mistake --> IT WAS ONE VARIABLE LETTER MESSING EVERYTHING UP!!!
--> Looking at CONSUMPTION (gross inland, not final)

**Get full dataset** Instead of handling six different, smaller datasets, I came to the conclusion that it makes more sense to have one big one and filter towards needs, so doing the same task for the third time now...

**Name your variables right** No sense in naming a column "formatted_values" if you have six of that...

**Reasons for not writing a function** Although I'm repeating the same steps over and over again, for each energy form, I deviated from writing a function, because without it, I have more control over in-between-steps (tweaking, cross-checking) and can access in-between-dfs for later invesigations more easily

**Filtering for selection and joining tables horizontally**
Cross-proving manually on paper, whether I can reproduce data in table-jpd with data from database --> check
Consumption EU average:
Renewable: 13%
Nuclear: 14%
Fossil:72 %
Subdivided:
21% Gas
34% Oil
17% Solid

Join tables horizontally
`joined_table = first_table.append(second_table)`

**Creating two sided bar graph**
Make new df, with only shares and adding up fossil shares to one
Manipulating renewable share, so it is negative and gets plotted to the other side
`df.plot.barh(stacked=True)`


**Data quest for GDP**: GDP or GDP per capita?
(Add picture)
Question: (GDP or population) linked to energy consumption linked to (renewable or renewable subsidies)?
Selection: x = GPD per capita, y = total energy consumption, z= share of renewables in energy consumption

--> subsidies would be really interesting to investigate, but data is difficult to get, so it's more time efficient for this task to stick with what is already there.

http://ec.europa.eu/eurostat/tgm/table.do?tab=table&init=1&language=en&pcode=tsdec100&plugin=1
Main GDP aggregates per capita
Table: nama_10_pc
Indicator: Gross domestic product at market prices
Unit: Chain linked volumes (2010), euro per capita

**Grab a row, based on index**
for example in order to make this row the column headers:
`gdp_df.columns = ((gdp_df.loc[2]))`

Note to self: not everything that looks like a number is a number!

Nex problem: Country spelling different between Eurostat Tables and Eurostat Database!!! Quest for the same table within the database

**Scatterplot with varying bubble size**
`df.plot.scatter(x='a', y='b', s=df['c']*200)`

**Labelling dots within a scatterplot**
Did not work: http://stackoverflow.com/questions/15910019/annotate-data-points-while-plotting-from-pandas-dataframe/15911372#15911372
DID WORK:
http://stackoverflow.com/questions/14432557/matplotlib-scatter-plot-with-different-text-at-each-data-point
Beware to check whether your index starts at 0, if not you need to add your first index number x to i within the for loop

**Annotation lines for scatterplot**
merge_gdp_consumption['GDP_per_capita'].mean(): 25419.354838709678
merge_gdp_consumption['GDP_per_capita'].median(): 20100.0
merge_gdp_consumption['consumption_allenergy'].mean(): 50287.060606060608
merge_gdp_consumption['consumption_allenergy'].median(): 22097.0

**Energy price data**
* Look at consumer instead of industry prices?
* It's incredible that if you use less energy, you have to pay more by kWh!!!
* Will try to visualize it as small multiples! #yay

TAX == "All included"
CURRENCY == "Euro"

Energy prices, industrial consumer: Eurostat nrg_pc_205
http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=nrg_pc_205&lang=en
CONSOM == Band IC 500MWh to 2000 MWh

Energy prices, domestic consumer: Eurostat nrg_pc_204
http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=nrg_pc_204&lang=en
CONSOM == Band DC 2500 to 500 kWh

**Small multiples**
Copy of Soma's code: http://jonathansoma.com/lede/data-studio/classes/small-multiples/long-explanation-of-using-plt-subplots-to-create-small-multiples/

.replace() with regex to change country names into something readable

Problems with merging energy prices for industry and households, bc merging on "GEO" (=country), however multiple time-value-pais for each country, with the time-key not being identical for each country and between the two df.
Fixed with creating a unique key by merging countryname and time-key into one and merging on that. Ugly, but worked.

### Questions:

* After having created a merged df and calculating a new column, plotting this column doesn't allow df columns as x labels, but only takes indices. However when plotting an original column, this change works. Ideas?

* in `df = df.drop('column_name', 1)` What does the 1 stand for? And: Can I delete several columns at once?
