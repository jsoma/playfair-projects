#CitiBIKE and MTA
##problems & solutions

###1
wow, could MTA's data download be less user-friendly? maybe.

#####problem: 
accidentally downloaded a 2011 version of mta performance data. it was in XML. i spent like 3 hours parsing it using ELEMENTREE

#####solution: 
i was confused about why MTA had not updated their performance data for five years, which led me to find a 2016 data set in csv. 

	
###2 

#####problem: 
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 81: invalid start byte

this is the error i got when i tried to use the pandas csv reader like this: 
`df=pd.read_csv('MTA_Performance_NYCT.csv')`

#####solution: 
including encoding argument
`df=pd.read_csv('MTA_Performance_NYCT.csv', encoding = "ISO-8859-1")`

###3 
#####problem: 
wanted to look at the values in a series, so that i could select rows by that value 

e.g. give me the rows where series.value = 'something'

#####solution: 
`series.values` is a thing 

###4 
#####problem: 
i don't know my question anymore because...i can't control for enough variables to narrow down any relationship between the flucuation in mta ridership and the flucuation in citibike ridership. 

#####solution: 
im going to throw out the MTA data set. i am going to focus on the CitiBike data set, and maybe add in the Station Entrances/Exits data set from MTA. 

**the project will now:**

group by subscriber and look at: 

- most popular origin points
	- 	are they farther from subway stops than less popular origin points? 
- most popular end points
	- 	closer to the subway stops than less popular end points? 
- what can i infer from this?
- compare most popular origin points to most popular end points 
	
###5 
#####problem: 
trying to create a histogram of `'tripduration'` by `'usertype'` which is whether the user is a subscriber or a customer. 

i tried using `.hist` 
	* everything was put into one bin
	* the scale was wrong on the x and y axis

#####solution: 
maybe i need to create classes. like define short, medium, long trips. 

###6 
#####problem: 
`'tripduration'` is a numpy.int64 type, *which i don't understand.* 

when i do a `.describe` on this column, i get  numbers that are in scientific notation. when i try to graph, i get huge values for `'tripduration'` like 3 million, and i dont know what the units are...milliseconds?

#####solution: 
i think that the values i am getting are in milliseconds. 
no, they're in seconds
	
###7 
#####problem: 
the `'tripduration'` range is HUGE from 1 minute to 52154 minutes. so this is a clarification/continuation of problem five.  

#####solution: 
i'm going to cut off about 10 percent of the data, any values above or below the outlier threshold (1.5*IQR).

once i trimmed my data set, histogram was much more informative/clear. 

###8
#####problem: 
so, now the question is: how do i match trip start points and end points to subway entrances/exits? 

i need to check if each ride's start or end station latitude,longitude matches any station's latitude, longtitude

#####solution: 
theoretically, i can solve this by: 

searching the subway data set by checking to see if any value in the series `citibike_df['start station location']` is in the series `subway_df['Latitude']]` 

im going to match on 4 decimal places based on this: http://gis.stackexchange.com/questions/8650/how-to-measure-the-accuracy-of-latitude-and-longitude/8674#8674 

	"The fourth decimal place is worth up to 11 m: it can identify a parcel of land. It is comparable to the typical accuracy of an uncorrected GPS unit with no interference."
	
-- 

update: i changed this two 2 decimal places, worth up to 1.1 km. im okay with this because i don't really think there are citibike or too many "different" subway locations (there are some) within 1.1 km of one another 

###9
#####problem: 
there are SO MANY citibike rows, so that looking through takes FOREVER. BUT i really need to look through to compare citibike start and end stations to subway stations. 

#####solution: 
**sort before searching** the citibike list of stations and the subway list of stations. because they are tuples (lat, long), i needed to sort by both items. then after sorting, i can say something like: 

	if citibike station in the list of subway entrances:
		citibike location is near a subway
	else: 
		citibike station is not near a subway
	

**take a sample** instead of doing this for 100,000s of rows, i took a 10,000 sample of citibike data frame

###10 
#####problem: 
What i have:
 
- two data sets (subscribers and customers) that have routes and counts of how often those routes appear. 
- two data sets (subscribers and customers) that have start stations and counts of how often those start stations appear. 
- two data sets (subscribers and customers) that have end stations and counts of how often those end stations appear.

What i want to do: 
	
i want to add geocoding to the data sets so that I can plot top ten routes, top ten starts, and top ten ends. 

the issue is that i don't know if there is a straightforward way to merge the route, start station, and end station counts to a data set 

#####another problem: 
 
- groupby object has no attribute `.to_csv` i.e. you can't export a group object as a csv..so when i try to group the date frame by route and add a count, it's not really possible. 
- groupby object does not support item assignment

i need a dataframe from a groupby object so i can export to a csv

#####solution: 
`df_new=df_old.groupby(['columnname']).size().reset_index(name='count')`

for some reason, `.reset_index` makes the series object (returned by `.size()`) a data frame.

so i then i was able to merge the frequency counts to the original data set, drop duplicates and keep unique rows with the counts of how often a start station, end station, or route occurred. 

###11
#####problem: 
i want to show the most popular routes. CartoDB does not do routes. 

#####solution: 

https://carto.com/blog/routing-sectionals/

- basically, use a different tool created by Mapzen

*...actually that's not the solution but an interesting tool, i may play with later.* 

**you actually can plot routes using the sql editor in cartodb: 
**
https://carto.com/blog/jets-and-datelines/
https://carto.com/blog/maptime-entry/

###12
#####problem: 

Okay, cartodb does do routes -- just not easily. Need a data set that has one line per location (so that's two line per ride -- one for the start location and one for the end), that identifies the points as being on the same route, and identifies the order in which those points should appear (e.g. start, order = 1; end, order = 2)

#####solution: 
tears. jk. 
i did a lot of data transformation to make the variables i needed 

###13 
#####problem: 
mapping is hard. 

while this sql query seems to do the job in cartodb. i am really unclear about what the code is doing, so i feel like i can't really confirm that the map is showing what i think it is...

	`SELECT field_1, route, count, cartodb_id, ST_MakeLine(the_geom_webmercator,
       (SELECT the_geom_webmercator
    	FROM mercyejiama.sub_ends_1
      	WHERE bikeid = c.bikeid and starttime=c.starttime and 
      	stoptime=c.stoptime LIMIT 1)) AS the_geom_webmercator 
    FROM mercyejiama.sub_starts_1
    AS c
    GROUP BY c.field_1, c.count, c.cartodb_id`

*field_1 is the route id. 

what i want it to show is a choropleth where the most popular routes are darkest and the least popular are lightest. I am not sure that the lines are showing a route (a start point and end point)

#####solution:
i turned on the labels, and each line was label with the appropriate route, so i guess its working. 


