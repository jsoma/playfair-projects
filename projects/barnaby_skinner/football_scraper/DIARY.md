# My Data Diary
## Main question: How difficult will in be, to convert the scraper to the Bundesliga

# Scraping issues:
This [player](http://www.transfermarkt.ch/victor-osimhen/leistungsdaten/spieler/401923/plus/0?saison=ges)
has no data. I built in try, except to deal with this. Surprising that a player being transfered to the
top German league has no data though.

#Scraping issues market:
For some reason one team turns up several times in the Dictionary. I deal with
this problem after changing the Dict into a Pandas DataFrame. With this function:
df_SL_transfers = df_SL_transfers.drop_duplicates()

Always beware of naming variables in functions.

#Prepping for Pandas
Nice function to drop any None values df_bundesliga_markt.dropna(how='all')
Have to be careful when working with the teams, the transfers came from. As SOME of them
are spelt differently, than the original entries.

Bayern München
Bor. Dortmund
VfL Wolfsburg
Bay. Leverkusen
1.FSV Mainz 05*
TSG Hoffenheim*
SC Freiburg*
FC Ingolstadt 04*
RB Leipzig
Hertha BSC
Bor. M'gladbach
Hamburger SV
FC Schalke 04*
E. Frankfurt
FC Augsburg
SV Werder Bremen*
TSG 1899 Hoffenheim*
1.FC Köln

FC Bayern München
Borussia Dortmund
VfL Wolfsburg
Bayer 04 Leverkusen
1.FSV Mainz 05
TSG Hoffenheim
SC Freiburg
FC Ingolstadt 04
RasenBallsport Leipzig
Hertha BSC
Borussia Mönchengladbach
Hamburger SV
FC Schalke 04
Eintracht Frankfurt
FC Augsburg
SV Werder Bremen
TSG 1899 Hoffenheim
1.FC Köln
