# Playfair Projects

This is where we'll be organizing our pitching/writing/etc process for all of the [Lede Program's](http://ledeprogram.com) Playfair projects.

* [Introduction](#introduction)
* [Contributing to Playfair](#the-process-in-general)
* [The Pitching/Submitting Process](#the-pitchingsubmission-process)
* [Story submission format](#story-submission-format)
* [Markdown](#markdown)
  
## Introduction

Playfair is a way for both current and previous students to stay on top of analysis, visualization, and all the arcane corners of data. Our goals are:

* **Create quality portfolio pieces** through a process that involves feedback and editorial oversight.
* **Give and receive feedback** to make our projects collectively better, along with making sure we're functional members of society.
* **Create documentation of our processes** so that others can learn from what we've created (and the really intense can reproduce and check our work)

Sounds good?

## Contributing to Playfair

> **NOTE:** Before being accepted, all pull requests must include [PR-CHECKLIST.md](PR-CHECKLIST.md) as the first comment, and have each box checked.

To contribute to Playfair, we use a combination of GitHub issues plus `git`'s forking ability. The steps are:

1. Create an issue for your pitch
2. Get your pitch approved
3. Create a story issue
4. Fork this repository
5. Work on the story on your fork, providing updates in the issue
6. When you're done, submit a pull request
7. Have it approved, rejoice

It seems painful, but it isn't as bad as it could be, I promise. Except the `git` part, of course.

## The pitching/submission process

You can read detailed instructions in [PITCHING.md](PITCHING.md), but a summary is below.

1. [Submit a pitch](https://github.com/jsoma/playfair-projects/issues/1) with [Pitch] in the issue title.
2. [Get some feedback](https://github.com/jsoma/playfair-projects/issues/1#issuecomment-234377726) and [respond to that feedback](https://github.com/jsoma/playfair-projects/issues/1#issuecomment-234379100).

3. You'll then get [editorial feedback and hopefully approval](https://github.com/jsoma/playfair-projects/issues/1#issuecomment-234380193).
4. [Create a story issue](https://github.com/jsoma/playfair-projects/issues/2) with [Story] in the issue title. **Include your pitch issue number**, mine was #1.
5. [Post updates](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234383998) and [get feedback](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234384424) and [post more updates](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234384733)
6. When you're done with your content, [send a pull request](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234384971) that **includes your story issue number** mine was #2
7. If everything looks good, your pull request will be approved and the [story issue closed](https://github.com/jsoma/playfair-projects/issues/2#issuecomment-234384994)

## Story submission format

You can read detailed instructions in [SUBMISSION.md](SUBMISSION.md). After you fork the repository, create your directories and complete your story, be sure to include the following in your pull request.

* a [correctly-formatted](SUBMISSION.md#storymd-format) `STORY.md` file
* `README.md`, summary of how you did your project
* `DIARY.md`, a disorganized mess keeping track of your process
* any images or code you used in the process of writing your story/building your visual

## Markdown

Markdown is just a way of writing text that doesn't rely on Word or Google Docs or whatever. It's exceptionally easy for computers to read. You can find detailed guides to Markdown *everywhere* on the ol' internet, such as [this one here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

A few markdown editors are below.

* [Dillinger.io](http://dillinger.io/) is great, but doesn't do images since it's on the web.
* [Mou](http://25.io/mou/) for OS X if you need automatic preview, [Atom](http://atom.io) if you don't
* I haven't used it, but [MarkdownPad 2](http://markdownpad.com/news/2013/introducing-markdownpad-2/) is for PC and looks pretty good.