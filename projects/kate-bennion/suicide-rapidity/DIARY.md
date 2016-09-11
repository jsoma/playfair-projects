A few years ago I wrote a story about how access to lethal means affects suicide rates (I come from a high gun-ownership and suicide-prevalent state). Some of the data I came across about how quickly people act after making the decision to end their life really stuck with me (almost half acted within twenty minutes of making the decision), and I wanted to depict that visually. It's a sensitive topic, but hopefully useful information for prevention/public health/awareness etc.

The data itself was fairly straightforward, but its qualitative nature led to some issues. I used the first of these studies:
https://www.hsph.harvard.edu/means-matter/means-matter/impulsivity/
They asked 153 survivors of near-lethal suicide attempts how soon after they made the decision they made their attempt. The answers broke down as follows:
24% said less than five minutes
24% said 5-19 minutes
23% said 20 minutes to 1 hour
16% said 2-8 hours
13% said 1 or more days

People didn't put exact times, just checked one of those categories. So answers fell into one of five widely-ranging categories. I tried several histogram mapping options, creating datasets to map based on time elapsed but also on number of people. This did not work. I eventually made proportional bin sizes and assigned values to the data based on where they fell, but was unhappy with the volume -- it made the smallest value (which took place over the longest time) look disproportionately huge.

I made a horizontal bar plot, which got the idea across, but wasn't able to convey a sense of time. 13% of the respondents stretched across 16 hours is very different than one bar the same width as the 24% five-minute value.

I then decided to make 288 5-minute-sized bins, and average the values for each category distributed across the appropriate number of bins and try and map it that way. This was also a fail, in both histogram and bar plot form.

(You can see these and other attempts for yourself if you like in the ipython notebook. Not all of them survived because I deleted a few in frustration.)

I may revisit this project after I hone my matplotlib skills a little more and/or come up with a different idea for visualizing the data, but it's time to move to the next thing for now.
