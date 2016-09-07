Scope
From BLM Platform, https://policy.m4bl.org

“The cradle-to-college pipeline has been systematically cut off for Black communities. According to the National Center for Education Statistics, 23 states spend more per pupil in affluent districts than in high-poverty districts that contain a high concentrations of Black students; and the U.S. Department of Education’s Office of Civil Rights shows persistent and glaring opportunity gaps and racial inequities for Black students. Black students are less likely to attend schools that offer advanced coursework, less likely to be placed in gifted and talented programs, more likely to attend schools with less qualified educators, and employ law enforcement officers but no counselors.”

Data
Basically a summary and some highlights of the data, according to the CRDC
http://www2.ed.gov/about/offices/list/ocr/docs/2013-14-first-look.pdf

The actual 2013-2014 school-level data
The school-level table layout documentation


Clip Search
U.S. Education: Still Separate and Unequal
The data show schools are still separate and unequal.
http://www.usnews.com/news/blogs/data-mine/2015/01/28/us-education-still-separate-and-unequal

Wikipedia: Racial achievement gap in the US
[w/ graphics]
https://en.wikipedia.org/wiki/Racial_achievement_gap_in_the_United_States

Recent Census Report on education gap
https://www.census.gov/content/dam/Census/library/publications/2016/demo/p20-578.pdf

Black students more likely to be suspended
http://www.reuters.com/article/us-usa-education-suspensions-idUSKCN0YT1ZO
https://www.theguardian.com/education/2016/jun/08/us-education-survey-race-student-suspensions-absenteeism

Pew: 5 Facts about Latinos in education
http://www.pewresearch.org/fact-tank/2016/07/28/5-facts-about-latinos-and-education/

Research perspective: Brookings: Unequal Opportunity: Race and Education
https://www.brookings.edu/articles/unequal-opportunity-race-and-education/

Government long aware of problem
https://nces.ed.gov/fastfacts/display.asp?id=72 

Issues with the data:
The shape of the data frame is challenging, there are 1929 rows describing the different attributes in the “contents” csv, and subsequently there are 1929 columns in the actual data. 95,507 is how many schools participated in the data, one row for each school.
df.shape
(95507, 1929)
Some of the string cell contents are really long, and pandas default settings truncates to … , so readability is a challenge. This helped:


#Changing display options to be able to see more column width/rows
pd.options.display.max_rows = 200
pd.options.display.max_colwidth = 100

Attempting to substantiate:
-Black public preschool children are suspended from school at high rates: Black preschool children are 3.6 times as likely to receive one or more out-of-school suspensions as white preschool children.
-Black children represent 19% of preschool enrollment, but 47% of preschool children receiving one or more out-of-school suspensions; in comparison, white children represent 41% of preschool enrollment, but 28% of preschool children receiving one or more out-of-school suspensions.
-Black boys represent 19% of male preschool enrollment, but 45% of male preschool children receiving one or more out-of-school suspensions.
-Black girls represent 20% of female preschool enrollment, but 54% of female preschool children receiving one or more out-of-school suspensions.

However, it seems that quite a few of the instances (out of nrows = 5000) are recorded as “-9”:
#Pre-school children (black, male) receiving one or more out-of-school suspension where value is -9
input: len(df_disc[df_disc['SCH_PSDISC_SINGOOS_BL_M'] == -9])l
output: 3677
#K-12 children without disabilities (black, male) receiving one or more in school suspension where value is -9
input: len(df[df['SCH_DISCWODIS_ISS_BL_M'] == -9])
output: 99

This means NaN according to Soma


