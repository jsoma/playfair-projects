# Story submission format

> Every story issue needs a checklist as the first comment. The checklist is available at [checklist-story.md](checklist-story.md).
> Every pull request needs a checklist as the first comment. The checklist is available at [checklist-pr.md](checklist-pr.md).

You'll be doing all of your edits in a fork of this repository.

Before you make your first project, you will need to create a folder inside of `projects` that is your name, for example I could create `projects/jonathan-soma`. Put dashes in the folder name instead of spaces, and please no non-alphanumeric characters.

Each project will go into a different subdirectory, e.g. `projects/jonathan-soma/project-about-whales` and `projects/jonathan-soma/crime-and-punishment`, etc.

Each project needs to include:

* **`STORY.yml`**, which includes a title and summary of your piece. We'll be using [a certain format for this file](#file-formats).
* **`STORY.md`**, the content of your story. We'll be using [a certain format for this file](#file-formats). Even if you don't include any words in your story, you'll need to include an image (and maybe a link to an interactive, if you have one).
* **any images/etc** you generated that you need for your story
* **`README.md`**, which is a writeup of how you did your project. It should include the title of your project, links to all data sources and a brief explanation of what you did
* **`DIARY.md`**, which should just be a running commentary by yourself to yourself about where you're looking for data, what kind of problems you're running into, and any changes you're making in the project (I was visualizing seal migration, but I found whale data so I'm using that instead!)
* **Any Jupyter Notebooks or other code you used.** Every time you run into an analysis problem in the Notebook, be sure to note it in `DIARY.md` (nobody wants to read all that code to find out your process).
* **Any files you exported from Python**, such as `.pdf` exports from `matplotlib

You'll also need a **`BIO.yml`** in your user folder describing who you are.

# File formats

## `.yml`, YAML

YAML - "Yet Another Markup Language" - is an easy way to list key/value pairs in a document. An example `STORY.yml` might be:

    title: "How Stephen Curry is Scamming the NBA"
    summary: "We looked at numbers involving Stephen Curry and you won't believe what we found. We won't believe it either, though, so we're all at a loss."
    authors:
      - Jonathan Soma
      - Jane Doe

Check [another example](http://www.yaml.org/start.html) if you'd like more information. If you use a `:` you might end up with problems, and if you only have one author **you don't need to specify the authors.**

## `.md`, Markdown

For all `.md` files we're going to be using the [standard Markdown format](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

For example, let's say I wrote a story about basketball that includes two images.

    Stephen Curry shoots a lot of threes. Is it too many threes? This chart thinks... possibly.
    
    ![](images/stephen-curry-scatterplot.png)
    
    But before you get too excited, this other chart things... possibly not.
    
    ![](images/stephen-curry-scatterplot2.png)

Not too crazy.

## Markdown

Markdown is just a way of writing text that doesn't rely on Word or Google Docs or whatever. It's exceptionally easy for computers to read. You can find detailed guides to Markdown *everywhere* on the ol' internet, such as [this one here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

A few markdown editors are below.

* [Dillinger.io](http://dillinger.io/) is great, but doesn't do images since it's on the web.
* [Mou](http://25.io/mou/) for OS X if you need automatic preview, [Atom](http://atom.io) if you don't
* I haven't used it, but [MarkdownPad 2](http://markdownpad.com/news/2013/introducing-markdownpad-2/) is for PC and looks pretty good.