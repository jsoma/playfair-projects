* pd.read_csv() read in a list as a string
* df.genres = df.genres.apply(literal_eval) solved it
* you can't do df['genres'].value_counts() with lists
* OMG CHRISTMAS IS THE WORST. Or maybe music is
* Find a way to use a smaller dataset
* save atom and close then reopen every once in a while to prevent crashing
* Oh I forgot to remove duplicate values from when I used calendar to pull out every week of every month. This means that sometimes the last week of a month is repeated. I used df.drop(df.index[[1,3]]) to remove the repeats.
* After you drop rows, you need to reset the index: df = df.reset_index(drop=True)
