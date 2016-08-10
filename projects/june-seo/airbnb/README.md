Airbnb dataset

I only grabbed one bedroom apartments by using 'bedrooms' columns and apartments those are rented as entire unit by using 'room_type' columns.
I used 'neighbourhood_cleansed' columns to group the data (instead of using 'neighbourhood' or 'neighbourhood_group_cleansed').
'price' was string with dollar sign. So I got rid of the dollar sign and changed it to float.
I assumed 67 percent occupancy rate which is an average reservation rate for NYC hotels. I multiplied 20 (20 days a month) to daily prices for listings.
Subtract the possible Airbnb monthly income from StreetEasy one bedroom apartment median asking rent by neighborhood.
