# Data diary

## Design choices
* **Axis + Axis Labels**: Myriad Pro, 14 pt
* **Text**:
  * Font: Shree Devanagari 714
  * Headline: Bold, 34 pt
  * Descriptive Text: Regular, 16 pt
  * Annotation: 12 pt
  * Source: 10 pt
* **Color**:
  * Purple Navy: #404e7c
  * Sunset Orange: #fe5f55
  * Turquoise: #4ce0d2
  * Sandstorm: #e8d245
  * Soap: #c6caed
  * Fall back for Soap: Silver Sand: #c2c1c2

## PITCH

#### Questions:
* How many total stops are there? How do they distribute over boroughs?
* How do stop-and-frisks evolve over time?
* Does race relate to being stopped?
* Do officers explain the reason for stopping someone?
* Does race relate to being frisked?
* Was an arrest made?
* Was the person summonsed?
* What was the the offense suspect was summonsed for?
* What type of physical police force is most abundant?
* How do the three most common types of police force relate to race?

#### Headlines:
* People of color get stopped more often by NYPD
* NYPD stop-and-frisk data screwed: No scheme to gather offense data
* Black and hispanic people are frisked more often

#### Data Source:
[NYPD, 2015](http://www.nyc.gov/html/nypd/html/analysis_and_planning/stop_question_and_frisk_report.shtml) How accurate can self-reported data be...?

## PROCESS:

## Thoughts/issues during production of this graphic series:

Maybe **I need to rethink my color-scheme**, as it seems too young & happy for rather serious topics like this

* (without having googled it yet) can we **define an individual** style in matplotlib, like 'ggplot' or 'fivethirtyeight', holding our own design and making things more efficient in future?

### Selecting variables from original dataset
Looking at 2015 data, selecting all variables to look at, based on the documentation file of the NYPD:

city
race
age
sex
explnstp -- did the officer explain reason for stop?
frisked -- was a person frisked
pf_* -- various forms of police force
arstmade -- was an arrest made?
arstoffn -- what was the arrest offense?
sumissue -- was a summons issued?
sumoffen -- what was the offense the person was summonsed for?
detailCM -- criminal code associated with entry
rf_vcrim -- REASON FOR FRISK - VIOLENT CRIME SUSPECTED
rf_othsw -- REASON FOR FRISK - OTHER SUSPICION OF WEAPONS
rf_attir -- REASON FOR FRISK - INAPPROPRIATE ATTIRE FOR SEASON

Looking at deciphering races:
B = Black
Q = Hispanic
W = White
P = Black Hispanic
A = Asians
Z = Other
I = American Indian/Alaska Native
X = Unknown

In some older datasets, U appears that is not annotated in the 2015 documatation. I guess it also is unknown. But then there's also 'other' - and what's the difference between other, unknown and U?


### Preparing the pie charts
**How to make a pie chart 2D instead of 3D?**
`plt.axis('equal')`

**Calculating the share of people being frisked**
White total: 2514
White frisked: 1387
White share frisked: 55%

Black total: 11950
Black frisked: 8515
Black share frisked: 71%

Hispanic total: 5090
Hispanic frisked: 3382
Hispanic share frisked: 66%

**How to adjust size of a pie chart?**
Use the `radius=` variable -- takes scalar values. However resizing only works, if you plot more than one pie from a given cell. If you only plot one pie per cell, it will always resize back to one.

Total stops black: 19950
Pie black radius = 1

Total stops hispanic: 5090
Relation to black: 0.43
(initially I made the mistake to set radius to 0.43
  instead of taking the squareroot from it, because it's an area)
Pie hispanic radius = sqrt(0.43) = 0.65

Total stops white: 2514
Relation to black: 0.21
Pie white radius = sqrt(0.21) = 0.46

If plotting **several pie charts at once, matplotlib overlays them**. Maybe that happens if you defined ax = ax anywhere before in the same notebook? Is there a way to prevent that (ie by setting ax for this chart back to its default -- however, googling did not reveal a default)?

##Time series
It took me ages, to figure out the code to get out the data needed for the graphs (total for each year, breakdown by race).

- drop columns
There's been a lot of reworking columns, adding new ones to a df, parsing etc -- so dropping columns came in very handy (no idea what the 1 stands for though? Also: can I run one line of code for several columns?)
`df = df.drop('column_name', 1)`

- make dates appear not in middle of year
When initially parsing the year into a datetime, I just used
`parsed_year = dateutil.parser.parse(year_str)`
This produced a problem when plotting: the data point of each year appeared in the middle of each year, bc the dates were parsed to the current month/date = end July.

To circumvent that in the first place, I couldn't help me other than setting back the date on my computer to the first of January to run the code.

With help of Stephan I figured, that there's a more elegant way to do it while parsing:
`parsed_year = dateutil.parser.parse(year_str+'-01-01')`

##Stacked bar chart
I stole the code from [Chris Albon's website](http://chrisalbon.com/python/matplotlib_percentage_stacked_bar_plot.html)without modifying a lot about it
* What does gca mean, what does zip do?

Way later I realized that I did a mistake: I stacked white, black, and hispanic to 100 percent -- ignoring all the others!

So I had to go back and rework the df to give me the numbers.
