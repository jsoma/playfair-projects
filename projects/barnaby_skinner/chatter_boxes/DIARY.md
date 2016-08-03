# Scraping the NR-Bulletin of Swiss Parliament

[Definition of what the Amtliches Bulletin actually is](https://www.parlament.ch/de/ratsbetrieb/amtliches-bulletin/amtliches-bulletin-erkl%C3%A4rt)

# Creating a DB of speeches by member of Parliament
Name of Speaker (Party, Canton), Speech. I want to end up with a dictionary that
looks like this:

    {'Name': 'Balti Glättli', 'Party': 'Grüne', 'Canton': 'ZH',
    'Speech': 'Die Welt ist nicht grün', 'Length': 568}

Possibly also create a column with the sex of the politician.

# Process
For the Summer Session of 2016, I need to use the the pages 81
(80 for computers) - 587 (586). Then convert this into one long string and extract
all the relevant information with findall, which will give me a list. Ideally, I
will end up with two lists, one for Name of Speaker Party and Canton.
And one with the speeches. The lists should all be the same length. I will then
iterate through all lists simultaneously, creating a dictionary as listed above.

# Tools
Using PyPDF2, which extracts the text. And then I am using Re to pull out
the relevant pieces of text.

## Example of code of PyPDF2
import PyPDF2
import re

pdfFileObj = open('Bulletin_Sommersession_NR_5004_1606.pdf', 'rb') #'rb' for read binary mode
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages

pageObj = pdfReader.getPage(93)  
Page_94 = pageObj.extractText()
Page_94

## Dealing with the document breaks:
used Regex to replace certain pattersn, is there a better way to do this?

## Regular expressions

Finding everthing in brackets, i.e. '(GL, AG)'
CODE: <Partei_Kanton = re.findall(r"\([A-Z]+, [A-Z][A-Z]\)", whole_Text)>

Get name from before the pattern (XY, XY), using a [negative outlook:](http://stackoverflow.com/questions/31713623/search-in-a-string-and-obtain-the-2-words-before-and-after-the-match-in-python)
Personen_name = re.findall(r'\w+\b\s+\b\w+(?=\s*\([A-Z]+, [A-Z][A-Z]\))', whole_Text)

!!!Problem, I'm sure there is a way to grab both the pattern (X+, XY) and the two words before,
I can't figure out how though. But as these lists are teh same length, I think it works anyway.
that come before.!!!

Important:
Name, Canton and one longer in the test, as they grab the text of the next speaker is not grabbed.

Using Zip to join three lists and make a dictionary out of them.

I am currently not including Markwalder, the president of the NR. This could be a separate search though.
Also Applies to the Bundesräte. How much time in Parlament to they have?

Problem with hyphens in names. This solved the problem. the pipe solved the problem:
[-\w|\w]


## Creating the dictionary

I might want to work with this, to see how many words the texts contain and come up with a number.
http://stackoverflow.com/questions/19410018/how-to-count-the-number-of-words-in-a-sentence


#Cleaning the data
Sometimes, for reasons I don't understand, a extra word is grabbed by the Regex
when getting the names, e.g.
motion
intérieur
fédérale
Etats
postulat
matière
initiative
Maintenir
sports
finances
Biffer
Etats
Maintenir
I am filtering this out with a replace, when setting up the dictionary. But this means, it makes
it more difficult to look at new or earlier Bulletins.

#Getting Gender of Nationalräte.
SHort research wasn't successful, so I decided to go down the path with Gender.c
This:
https://pypi.python.org/pypi/SexMachine/
And this:
https://pypi.python.org/pypi/estimate.gender
Just running the pip command the system demanded this:
RuntimeError: could not find boost's `version.hpp' - have you installed Boost on this machine?
So I installed it:
http://www.boost.org/doc/libs/1_57_0/doc/html/quickbook/install.html
No I get this:
Command "python setup.py egg_info" failed with error code 1 in /private/var/folders/g9/mnwc58dj3n58gw3pryxbmyzm0000gn/T/pip-build-y8phkomm/bob.blitz/





But sget this:
Command "python setup.py egg_info" failed with error code 1 in /private/var/folders/g9/mnwc58dj3n58gw3pryxbmyzm0000gn/T/pip-build-_dih94qi/bob.blitz/
