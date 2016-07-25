# Story submission format

You'll be doing all of your edits in a fork of this repository.

Before you make your first project, you will need to create a folder inside of `projects` that is your name, for example I could create `projects/jonathan-soma`. Put dashes in the folder name instead of spaces, and please no non-alphanumeric characters.

Each project will go into a different subdirectory, e.g. `projects/jonathan-soma/project-about-whales` and `projects/jonathan-soma/crime-and-punishment`, etc.

Each project needs to include:

* **`STORY.md`**, the content of your story. We'll be using [a certain format for this file](#storymd-format). Even if you don't include any words in your story, you'll need a title and to include your image via the appropriate markdown tag.
* **any images/etc** you generated that you need for your story
* **`README.md`**, which is a writeup of how you did your project. It should include the title of your project, links to all data sources and a brief explanation of what you did
* **`DIARY.md`**, which should just be a running commentary by yourself to yourself about where you're looking for data, what kind of problems you're running into, and any changes you're making in the project (I was visualizing seal migration, but I found whale data so I'm using that instead!)
* **Any Jupyter Notebooks or other code you used.** Every time you run into an analysis problem in the Notebook, be sure to note it in `DIARY.md` (nobody wants to read all that code to find out your process).
* **Any files you exported from Python**, such as `.pdf` exports from `matplotlib

# `STORY.md` format 

For `STORY.md` we're going to be using the [standard Markdown format](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), but with a little  "Front Matter" section added to the start to help with online presentation. You can read more about [Front Matter here](https://jekyllrb.com/docs/frontmatter/) if yo uwant, but it's pretty easy.

For example, let's say I wrote a story about basketball that includes two images.

    ----
      title: How Stephen Curry is Scamming the NBA
      summary: We looked at numbers involving Stephen Curry and you won't believe what we found. We won't believe it either, though, so we're all at a loss.
      authors:
        - Jonathan Soma
        - Jane Doe
    ----

    Stephen Curry shoots a lot of threes. Is it too many threes? This chart thinks... possibly.
    
    ![](images/stephen-curry-scatterplot.png)
    
    But before you get too excited, this other chart things... possibly not.
    
    ![](images/stephen-curry-scatterplot2.png)

You'll want to include the appropriate dashes to mark the Front Matter section, along with a `title` and a `summary`.

If you are the only author, you don't need to list any authors at all. If you have multiple authors, make a list like above.