## Design choices
* **Font** Raleway Family
  * Header: Heavy Black, 34 pt
  * Descriptive Text: Light, 16 pt
  * Axis Labels: Regular, 12 pt
  * Annotation: Regular, 12 pt
  * Source: Regular, 10 pt
* **Color**:
  * Purple Navy: #404e7c
  * Sunset Orange: #fe5f55
  * Turquoise: #4ce0d2
  * Sandstorm: #e8d245
  * Soap: #c6caed
  * Fall back for Soap: Silver Sand: #c2c1c2


# PITCH
"There's lots of money for refugees, but only few for pensioners and families." is one of the arguments of xenophobic people in Germany.
I would like to know whether that's actually true and dive into government expenditures on these areas.
* [Absolute + per capita] government expenditures for refugees/pensioners/social benefit recipients
* Breakdown to one person: How much does a refugee/pensioner/social benefit recipient get?

On a first glimpse it looks like as if there's no data evidence for the claim made at the beginning:
Roughly 4 billion dollar are spend on refugees, vs 93 billion for pensioners and 34 billion for social benefits, 7 billion for family support.

On a recipient perspective breakdown, a social benefit recipient receives 399 euros per month, a refugee 130 euros.

**Data source**
[German government](https://www.bundeshaushalt-info.de/#/2016/soll/ausgaben/einzelplan/0603.html)

**Clip search**
As far as I can see this has not been done before by German media as a visual yet.
There's a long story about by-federal-state breakdown [by Die Welt](http://www.welt.de/wirtschaft/article154060168/Ob-Bayern-oder-Bremen-ist-fuer-Fluechtlinge-ein-grosser-Unterschied.html), just listing numbers, not making any charts.

And there's another story by Zeit Online, including a [card game (cards 15, 17 and 18)](http://www.zeit.de/politik/deutschland/2015-09/fluechtlingshilfe-deutschland-massnahmen-sozialneid-kommunen), that highlights this topic but doesn't really cover it visually either.

**Headline suggestions**
* Xenophobic arguments debunked
* No need for social envy towards refugees
* 3 simple barcharts to counter xenophobic arguments
* 3 simple bar charts is all it takes to debunk xenophobic claims

# PROCESS

## Data problems:
* The German ministry of Finance told me where to find the dataset behind their fancy graphic.
However, the dataset does not contain the data visualized...

* There are clips on how much benefits asylum seekers get, however not datasets.
[Reuters article, listing benefits received by country](http://www.reuters.com/article/us-europe-migrants-benefits-factbox-idUSKCN0RG1MJ20150916)
[Euro News article, including a map, based on (?) the Reuters article](http://www.euronews.com/2015/09/16/which-european-countries-offer-the-most-social-benefits-to-migrants)

* There are also pdfs collecting the above information, however, outdated
[2009](http://ec.europa.eu/dgs/home-affairs/what-we-do/networks/european_migration_network/reports/docs/ad-hoc-queries/protection/151._emn_ad-hoc_query_cash_and_other_benefits_granted_to_asylum_applicants_27aug2009_wider_dissemin_en.pdf)
[2011](http://ec.europa.eu/dgs/home-affairs/what-we-do/networks/european_migration_network/reports/docs/ad-hoc-queries/protection/351_emn_ad-hoc_query_cash_and_other_benefits_for_asylum_seekers_4nov2011_wider_dissemination_en.pdf)

* To give it a positive twist, include *somehow* these studies highlighting how economy benefits from migrants
[Economist](http://www.economist.com/news/finance-and-economics/21688938-europes-new-arrivals-will-probably-dent-public-finances-not-wages-good-or)
[Brookings](https://www.brookings.edu/2015/09/16/much-ado-about-nothing-the-economic-impact-of-refugee-invasions/)
[New Yorker](http://www.newyorker.com/news/john-cassidy/the-economics-of-syrian-refugees)
[Reuters](http://www.reuters.com/article/us-crisis-lebanon-refugees-idUSBRE93G0MW20130417)

**Likely solution:**
- Manually get all the data from the ministry's website
- Go through the above mentioned clips and pdfs and gather data

### Data needed
* First get data for Germany -- one row
* If time left -- more European countries (selection? Sweden + eastern + southern European country?)

*Table 1 structure/columns*


country **GERMANY**
number of social benefits recipients  [Data Source](http://de.statista.com/statistik/daten/studie/1396/umfrage/leistungsempfaenger-von-arbeitslosengeld-ii-jahresdurchschnittswerte/)
number of refugees/asylum seekers [Data Source](http://www.welt.de/politik/ausland/article156356943/Nur-ein-Land-nimmt-mehr-Fluechtlinge-auf-als-Deutschland.html)
number of pensioners [Data Source, (2014)](http://www.welt.de/wirtschaft/article149155412/Zehntausende-Rentner-werden-2016-steuerpflichtig.html)

government money that goes into pensions [Data Source, Unique identifyer 'Haushaltsstelle': 1102](https://www.bundeshaushalt-info.de/#/2016/soll/ausgaben/einzelplan/11.html)
government money that goes into social security [Data Source, Unique identifyer 'Haushaltsstelle': 1101](https://www.bundeshaushalt-info.de/#/2016/soll/ausgaben/einzelplan/11.html)
government money that goes into refugee sector/immigration [Data Source, Unique identifyer 'Haushaltsstelle': 0603+0633](https://www.bundeshaushalt-info.de/#/2016/soll/ausgaben/einzelplan/06.html) and [Ministry of Finance to Fedeal states: 670 euro per refugee per month](http://www.welt.de/wirtschaft/article154060168/Ob-Bayern-oder-Bremen-ist-fuer-Fluechtlinge-ein-grosser-Unterschied.html)


government money that goes into pensions/per pensioner [calculated from above]
government money that goes into social security/per social benefit recipient [calculated from above]
government money that goes into refugee sector/immigration per refugee [calculated from above]

country **SWEDEN**
[Number of refugees + Budget](https://www.theguardian.com/global-development/2015/nov/05/sweden-could-redirect-60-of-development-aid-funding-to-refugee-crisis)

country **LEBANON**
[Number of refugees](http://data.unhcr.org/syrianrefugees/country.php?id=122)
[Money spend on refugees](http://www.state.gov/j/prm/releases/remarks/2014/219388.htm)

*Table 2 structure/columns*

country
average living costs

PENSIONERS
non-cash benefits
cash benefits

SOCIAL BENEFIT RECIPIENTS
non-cash benefits
pocket money adults

REFUGEES
non-cash benefits
pocket money adults

-- abandoned as well, only found one data source and no second one to back it up. And that's kind of risky esp. with this topic.

**Icons** from [the Noun Project](https://thenounproject.com/)
* House [by Creative Stall](https://thenounproject.com/search/?q=house&i=123410)
* Food
  - [Bowl by Creative stall](https://thenounproject.com/search/?q=food&i=105906)
  - [Apple by Creative Stall](https://thenounproject.com/search/?q=food&i=178879)
  - [Bread by Hugo Alberto](https://thenounproject.com/search/?q=bread&i=537812)
* Toothbrush [by Tomas Knopp](https://thenounproject.com/search/?q=toothbrush&i=539632)
* Clothes -- [T-shirt by Timur Zima](https://thenounproject.com/search/?q=clothes&i=16914)

*Table 3 -- structure*

for Germany, Sweden, Lebanon:
  country
  household budget
  total govt spending on refugees (see table 1)

-- abandoned this one, no consistent data basis for it.
