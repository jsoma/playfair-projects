# BOTica analysis: The 8 most wanted medicines.

### Possible questions to ask the data:

  - What states/cities are people tweeting from?
  - What is the medicine that most people are asking for?
  - Is the data clean? Are people making grammar mistakes when asking for a medicines?
  - Who is donating medicines? Where are they from? Are they part of an organization?
  - How is the communication between users. Do they meet to exchange the medicines? Do we know that? Does that conversation take place outside Twitter?


### Problems I encountered

  - Repetitive requests from the same user for the same medicine. I used TextBlob to find the most common words found in BOTica's tweets and from there find the medicines most people are asking for. I get notifications everytime someone sends BOTica a message so I am familiar with the medicines that venezuelans are asking for.  After running the text through TextBlob,  I saw that the word 'Alactin' appeared 3 times and I knew something was wrong because I knew that only one user had asked for that medicine. I went back to the data and realized that the same user had sent the same message 3 times in the past 12 days. Same case with many other medicines.
  Because of this problem, I had to manually create a dataset in excel, inputing 1 request only per medicine per user.

  - People also made grammar mistakes when asking for medicines. I had to manually check online for the correct name of all the medicines.

  - Not all the users provide the same info, some provide emails, others phone numbers, and others don't specify where they are from. This is problematic because I can't analyse the data to look for the states where most messages are coming from, etc. Every Tweet has info about location, but for some the field is empty, I am supposing location most be enabled in the person's cellphone/computer when the message is sent.

### Design decisions
  - I wanted the graph to look as clean as possible. I knew I had to include a big legend with all the Twitter handles so I wanted to have as much white space as I could to balance it out.
  - I got rid of the grids and all tick marks except the ones on the bottom x axis (I thought they helped orient the eye).
  - For the colors, I made a quick search for medicine boxes online and chose the most common colors (pastels greens and blues and sometime orange). Someone suggested I stick with the colors for BOTica (yellow, blue, and red), also the colors of the Venezuelan flag, but it just did not look right to me.
  - For inspiration I looked at a number of graphs from The Guardian's DataBlog
