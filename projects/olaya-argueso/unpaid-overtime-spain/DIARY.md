## Unpaid overtime in Spain

The National Institute of Statistics gathers a lot of data about the labour market in Spain. One of the things theey measure is the amount of overtime workers do in Spain, both paid and unpaid. Here is a [link to the data](http://www.ine.es/dynt3/inebase/es/index.htm?padre=982&capsel=985).

After looking for inspiration, I found this image, which I will try to replicate:

![](graphs-inspiration/inspiration_line_graph_15-data.jpg)

I would like to see both the minor and the major ticks (now, matplotlib only gives me the major ticks for the year, but since the data follow a clear pattern depending on the quarter, I want to be able to visualize them). I have tried changing the index to be the date and resampling (no success: it shows the minor ticks, but no the lines of the graph. With *groupby* based on the index, it gives me everything, except the minor ticks! I will try creating two different graphs and somehow overlapping them in AI.

The solution mentioned above worked for me.

I wanted to check which % of the working hours were unpaid overtime for each occupation. However, the data for the unpaid overtime are quarterly total hours, while the 'regular' working hours for each occupation are weekly. When trying to do a basic mathematical operation to turn weekly hours into quarterly, the figures did not match. Looking into the methodology, the National Statistics Institute does not explain how they add up the hours, so I cannot do the conversion in a reliable way. I have therefore quit this idea.

After some feedback, I have made my texts whiter and bigger, have 'bolded' certain lines in my second graph (the ones that are really important), and reduced part of the text to make figures clearer (even if I lose a little bit of precision and detail).
