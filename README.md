# Playfair Projects

This is where we'll be organizing our pitching/writing/etc process for all of the [Lede Program's](http://ledeprogram.com) Playfair projects.

## Introduction

Playfair is a way for both current and previous students to stay on top of analysis, visualization, and all the arcane corners of data. Our goals are:

* **Create quality portfolio pieces** through a process that involves feedback and editorial oversight.
* **Give and receive feedback** to make our projects collectively better, along with making sure we're functional members of society.
* **Create documentation of our processes** so that others can learn from what we've created (and the really intense can reproduce and check our work)

Sounds good?

## The Process in General

To contribute to Playfair, we use a combination of GitHub issues plus `git`'s forking ability. The steps are:

1. Create an issue for your pitch
2. Get your pitch approved
3. Create a story issue
4. Fork this repository
5. Work on the story on your fork, providing updates in the issue
6. When you're done, submit a pull request
7. Have it approved, rejoice

It seems painful, but it isn't as bad as it could be, I promise. Except the `git` part, of course.

## The Pitching/Submitting Process

The projects pitching+story creation process involves several steps, with lots of feedback! They mostly take place on the [Issues section](https://github.com/jsoma/playfair-projects/issues) of the repository. They're called issues but we're using them to track pitches, feedback, and story progress.

Each issue will have a series of **labels** attached to it, like `Type: Pitch` or `Requested: Assistance`. While you can't assign these - people in charge of this repository can - you can say things like [Pitch] or [Request assistance] to suggest that people tag the repositories.

### Step 1: The Pitch

First, you'll need to pitch your story by opening a new issue.

[Here is an example pitch](https://github.com/jsoma/playfair-projects/issues/1), which includes a data source, a "my piece will look like this" image, and a request to find some more data. Notice the [Pitch] [Data request] in the submission title.

Include images by pasting them into the text area, or dragging them from your desktop.

### Step 2: Feedback

You'll need to go through several rounds of feedback: first, peer feedback and then editorial feedback. After each round of feedback you'll need to respond. It's best if you respond particularly to what the person was saying, but a "thanks!" is sometimes good enough.

You can see an [an example of feedback](https://github.com/jsoma/playfair-projects/issues/1#issuecomment-234377726) and [an example of a pitcher response](https://github.com/jsoma/playfair-projects/issues/1#issuecomment-234379100) on the sample issue. I know it's all done by one person, but *I am very sorry I don't have multiple github accounts*.

### Step 3: Editorial feedback and approval

After your editorial feedback, you may need to revise your pitch a little more. Eventually you'll (hopefully) be approved, and you can move on to the story process.

[This is a pitch being approved](https://github.com/jsoma/playfair-projects/issues/1#issuecomment-234380193). Once the pitch is approved and the story issue is created, an admin will close down the pitch issue.

### Step 4: Creating the story issue

Once your story is approved, you can open up a new issue. [Here is an example](https://github.com/jsoma/playfair-projects/issues/2), you'll note I titled it with [Story] to suggest a story tag.

The story issue is a lot like your pitch issue, except you incorporate everything that changed over the course of the discussion. Maybe you found new data sets or new points of view - explain that here, pretend that whoever is reading this never saw your pitch.

You'll also want to link your pitch at the top of your story - you can do that by typing a # and then your pitch's issue number. You can find the issue number in the URL. The sample one is at `https://github.com/jsoma/playfair-projects/issues/1`, so the link can be made by typing #1. It will automatically link to your pitch.

### Step 5: Posting updates

As you work on your story, add updates! Little image previews or links to your forked repository would be great. [Here is an example of an update](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234383998).

### Step 6: More peer feedback

Now that you've been approved, the feedback should be a little more particular. "This particular color is hard to read" or "you might want to look at how you're treating that categorical variable." While you don't have to do what other people say, it's definitely good to think about.

[Here is some feedback from the sample story issue](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234384424).

### Step 7: Requesting approval

Once you're done, send a pull request with your new content. **Make sure you include your story's issue number, like #2**. Someone might also label that your story issue needs editorial approval.

[Pretend I sent a pull request here](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234384971), which then gets approved and the story issue is finally closed.

### Recap: Just tell me real quick

1. [Submit a pitch](https://github.com/jsoma/playfair-projects/issues/1) with [Pitch] in the issue title.
2. [Get some feedback](https://github.com/jsoma/playfair-projects/issues/1#issuecomment-234377726) and [respond to that feedback](https://github.com/jsoma/playfair-projects/issues/1#issuecomment-234379100).

3. You'll then get [editorial feedback and hopefully approval](https://github.com/jsoma/playfair-projects/issues/1#issuecomment-234380193).
4. [Create a story issue](https://github.com/jsoma/playfair-projects/issues/2) with [Story] in the issue title. **Include your pitch issue number**, mine was #1.
5. [Post updates](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234383998) and [get feedback](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234384424) and [post more updates](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234384733)
6. When you're done with your content, [send a pull request](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234384971) that **includes your story issue number** mine was #2
7. If everything looks good, your pull request will be approved and the [story issue closed](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234384994)

## The Files

You'll be doing all of your edits in a fork of this repository.

Before you make your first project, you will need to create a folder inside of `projects` that is your name, for example I could create `projects/jonathan-soma`. Put dashes in the folder name instead of spaces, and please no non-alphanumeric characters.

Each project will go into a different subdirectory, e.g. `projects/jonathan-soma/projects1` and `projects/jonathan-soma/projects2`, etc.

Each project needs to include:

* `STORY.md`, the content of your story. We'll be using a certain format for this file (see below). Even if you don't include any words in your story, you'll need a title and to include your image via the appropriate markdown tag.
* any images/etc you generated that you need for your story
* a `README.md`, which is a writeup of how you did your project. It should include the title of your project, links to all data sources and a brief explanation of what you did
* a `DIARY.md` which should just be a running commentary by yourself to yourself about where you're looking for data, what kind of problems you're running into, and any changes you're making in the project (I was visualizing seal migration, but I found whale data so I'm using that instead!)
* Any Jupyter Notebooks or other code you used. Every time you run into an analysis problem in the Notebook, be sure to note it in `DIARY.md` (nobody wants to read all that code to find out your process).
* Any PDF or SVG files that you exported from `matplotlib`, before editing them

## `STORY.md` format 

For `STORY.md` we're going to be using the [standard Markdown format](http://dillinger.io/), but with a little  "Front Matter" section added to the start to help with online presentation. You can read more about [Front Matter here](https://jekyllrb.com/docs/frontmatter/), but it's pretty easy.

You'll want to include the appropriate dashes to mark the Front Matter section, along with a `title` and a `summary`.

If you are the only author, that's all you need to include. If you have other authors, make a list like below.

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

Note that I don't know anything about basketball. Probably should have said that before.

## Markdown editors

* [Dillinger.io](http://dillinger.io/) is great. Just use that.
* [Mou](http://25.io/mou/) for OS X if you need automatic preview, [Atom](http://atom.io) if you don't
* I haven't used it, but [MarkdownPad 2](http://markdownpad.com/news/2013/introducing-markdownpad-2/) is for PC and looks pretty good.