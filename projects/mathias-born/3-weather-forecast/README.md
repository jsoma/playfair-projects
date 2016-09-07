# Meteotest

Most people rely on it -- even if they would't call this information reliable. How good or bad is the weather forecast in reality? I will scrape some information of the five days forecast and compare it to the mesurements five days later.  

## Background

### Provider

There are four major provider for forecasts in Switzerland. 

- [MeteoSchweiz](http://www.meteoschweiz.admin.ch): The Federal Office of Meteorology and Climatology MeteoSwiss is still the most important and biggest provider of weather forecasts. The most important customer is the newspaper [NZZ](http://nzz.ch).
- [SRF Meteo](http://www.srf.ch/meteo): Swiss National Television and Radio. Head: Thomas Bucheli. 
- [Meteotest](http://www.meteotest.ch): Meteo provider from Bern. Most important customer: [Somedia](http://www.somedia.ch), publisher of 'Südostschweiz', 'Schweiz am Sonntag' etc.
- [MeteoNews](http://meteonews.ch): Customer are most of the Swiss dailies (Blick, 20 Minuten, Tages-Anzeiger, Berner Zeitung) and the private radio stations. Founded by Peter Wick.

Additional:

- MeteoGroup: A provider from Germany, buyer of Jörg Kachelmanns Meteomedi.
- Kachelmannwetter: A new project by Jörg Kachelmann. 

### Websites to scrape

- [MeteoSchweiz](http://www.meteoschweiz.admin.ch/home.html?tab=overview): Complex website hiding the necessary information behind graphs. 
- [SRF Meteo](http://www.srf.ch/meteo/lokalprognose?id=417255326): Complex website hiding the necessary information. 
- [Meteotest](https://meteotest.ch/wetter/ortswetter/Bern): Does not have information about how the weather develops during the day. 
- [MeteoNews](http://meteonews.ch/en/Weather/G2661552/Bern): The easiest one to scrape. 

### Values to scrape:

Values five days from now all three hours (03:00, 06:00, 09:00 etc.)

- Description
- Temperature
- Rain (amount)
- Wind

### Measured values

Mesurements from the Federal Office of Meteorology. Since they are hard to access, we are using the [API of Netcetera](http://data.netcetera.com/smn). Alternative: [Our own logger from a previous project](https://github.com/philippkueng/meteo-logger).

### Reading:

- Hanspeter Guggenbühl: [Wie der Markt mit dem Wetter spielt](http://www.tageswoche.ch/de/2015_28/schweiz/692792/)
- Stiftung Warentest: [Online-Wetterdienste im Test](https://www.test.de/Online-Wetterdienste-im-Test-Welche-Portale-die-besten-Prognosen-liefern-4696702-0/)
