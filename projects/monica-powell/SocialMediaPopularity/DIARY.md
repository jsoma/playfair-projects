I was excited to work with Google Trends data but it seemed to need a lot of cleaning (each week was a date range) and did not provide actual numbers (everything was scaled in relation to the highest point on graph -- with the highest point being 100).

Whereas, with the New York Times data I could look at the actual volume associated with each social media site for a given time period and paint a more accurate picture of the data.

I also learned that using groupby and x=year together, ignores the x value and instead overrides it with the index. In order to resolve this issue I had to use a for loop to graph multiple subplots.
---

After reviewing my data I decided to collect NYT data for every quarter of each year from 2005-2016. Instead of just collecting a sum for each year (thus multiplying the number of data points by 4).
