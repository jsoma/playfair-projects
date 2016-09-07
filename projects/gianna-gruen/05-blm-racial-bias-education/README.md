## Intention:
The initial idea was from Georgia Kromrei, to substantiate the claims the [Black Lives Matter movement](https://policy.m4bl.org/reparations/) with visuals.

I picked three of them:
1) "Black students are less likely to be placed in gifted and talented programs"

2) "Black students are less likely to attend schools that offer advanced coursework"
I adjusted this one to also look at enrolement rates, as in 1)

3) "Black students are more likely to attend schools with less qualified educators, and employ law enforcement officers but no counselors."
This one would actually need to be broken down in share of black students in relation to
3.a) teacher Experience
3.b) number of counselors
3.c) number of law enforcement officers

## Data source:
The data is from the US Department of Education and refers to the educational period of 2013/2014. It was released at the beginning of August 2016.
All datasets and the various documentation files can be found [on this website](http://www2.ed.gov/about/offices/list/ocr/docs/crdc-2013-14.html)

## Process:
For 1) and 2) I looked only at schools with at least 5% black students, because otherwise all the 0-values would skew the image.

for 3.a) The qualification of a teacher was measured by the presence or absence of a certificate and their experience was differentiated by one versus two years of teaching experience. Because both seem rather imprecise measures to assess a teacher"s quality, I decided to skip this claims

for 3.b) The difficulty was that the number of counselors were given in FTE (full time equivalents) The most frequent counts were 0 and 1 -- and then a lot of decimals inbetween. I decided to round these numbers to divide it into two categories: the presence or absence of a counselor. Rounding the inbetween values did not change the relation of 0 to 1 counts.

Analysis showed that the claim of BLM - black students were more likely to be in schools with no counselor - was not true. In fact, there was on average a third more black students in schools with a counselor compared to those without a counselot.

for 3.c) The data was only present in a "YES" or "NO" format (so presence or absence of a law enforcement officer) -- if the value was "YES" it was not specified how many law enforcement officers were present at that given school. This data is said to be gathered for the next school census 2015/16.
