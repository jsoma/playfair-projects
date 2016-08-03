The purpose of this analysis is to understand the statistics regarding the size(sq.meter) of apartments in South Korea metrocities using Python.

Inspired link : https://www.washingtonpost.com/world/after-decades-of-economic-growth-south-korea-is-the-land-of-apartments/2013/09/15/9bd841f8-1c55-11e3-8685-5021e0c41964_story.html

###  Analysis

There are  8 metropolitan cities in South Korea. There are apartments in other locations/provinces, however, most apartments are concentrated in Metro Cities and because the amount of data is relatively small, they were ignored from the analysis. (Kyungi province was later added.)

According to the Korean Government, apartments larger than 914 sq ft are considered "large residential property" for tax purpose. (The calculation of tax is more complex, but they charge property tax  0.15% more or less.) I decide to figure out the number of such large apartments in our data set and its ratio to the entire market.

(1) The ratio of the large residential property in South Korea

<p align="center">
![output-graph_01](https://cloud.githubusercontent.com/assets/19519829/17150940/663b13f8-533f-11e6-97be-15053abdbfc4.png)


![output-graph_01_01](https://cloud.githubusercontent.com/assets/19519829/17150543/e1ef9048-533d-11e6-9c40-6fbd17c83c00.png)


(2) Factors Correlated to the Large Apartment Ratio
Tested correlation of two factors: city budget and average GDP of the city toward large apartment ratio.

The ratio of Large Apartments were relatively consistent regardless of the city, and that the number of large apartments is not correlated with the Average GDP of the city.

<p align="center">
![output-graph_02_modified](https://cloud.githubusercontent.com/assets/19519829/17112883/f5faee02-5275-11e6-838f-c7f9896b4018.png)

===========================================
Data location, Study Material Location, and Origin of Codes 
All Right reserved. Source, Data, Coding Method to orginal location of link mentioned below.

- Korean Apartment(Residential Property) Management Info System : http://www.k-apt.go.kr
- South Korea Ministry of Land and Infrastructure and Transportation : http://rt.molit.go.kr
- LEDE Program : http://ledeprogram.com/
- Haeshik : http://nbviewer.ipython.org/gist/hyeshik/cf9f3d7686e07eedbfda?revision=6
- Openwings : http://goodvc.tistory.com/category/%EB%82%98%EC%9D%98%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D
