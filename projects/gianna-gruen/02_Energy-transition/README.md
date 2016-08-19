Data source: Eurostat database
Tables:
[nrg_100a -- energy consumption, absolute](http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=nrg_100a&lang=en)
[nama_10_pc -- real GDP per capita](http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=nama_10_pc&lang=en)
[nrg_pc_204 -- energy consumption, domestic](http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=nrg_pc_204&lang=en)
[nrg_pc_205 -- energy consumption, industrial](http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=nrg_pc_205&lang=en)
For details on data selection and data formatting process: see DIARY.md

For the first graphic, the **two sided bar graph showing the share of energy type in total consumption**, I used data from nrg_100a. I downloaded the whole dataset and read it in with pandas and then filtered for to the demand of each task.

For the second graphic, the **scatter plot with varying bubble size linking energy consumption, GPD per capita, reneawle share**, I used data the previous data and added the nama_10_pc data.
I first made a stacked bar chart with all shares of energy type in total consumption using `df.plot.barh(stacked=True)` to see whether it works.

Then I made the part of the data I wanted to have plotted to the other side negative and plotted anew.
All mirrowing and changing was done in Adobe Illustrator.

To *vary the bubble size*, I used this line of code `df.plot.scatter(x='a', y='b', s=df['c']*x)`
With x you can artificially scale up bubble size (in my case: x=30)

To *annotate the bubbles*, I used [this code from Stack Overflow (found by Mercy Emelike)](http://stackoverflow.com/questions/14432557/matplotlib-scatter-plot-with-different-text-at-each-data-point):
`y=[2.56422, 3.77284,3.52623,3.51468,3.02199]
z=[0.15, 0.3, 0.45, 0.6, 0.75]
n=[58,651,393,203,123]

fig, ax = plt.subplots()
ax.scatter(z, y)

for i, txt in enumerate(n):
    ax.annotate(txt, (z[i],y[i]))`
Beware to check whether your index starts at 0, if not you need to add your first index number x to i within the for loop.

All further annotation was done in Adobe Illustrator.

For the third graphic, the **small multiples on energy prices**, I used this code from [Jonathan Soma](http://jonathansoma.com/lede/data-studio/classes/small-multiples/long-explanation-of-using-plt-subplots-to-create-small-multiples/)
While plotting two lines in one small multiple, I had some data issues (see DIARY.md for details) and countries for which only data for one line were provided, where not plottet. Thus, I made one small multiple for energy consumer prices (one for industry prices) and the plotted both at once. In Illustrator, I filled up the missing two graphics (Iceland and Albania) from the first small multiples. 
