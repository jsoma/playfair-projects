## Design choices
* **Font** Raleway Family
  * Header: Heavy Black, 34 pt
  * Descriptive Text: Light, 16 pt
  * Axis Labels: Regular, 12 pt
  * Annotation: Regular, 12 pt
  * Source: Regular, 10 pt
* **Color**:
  * Purple Navy: #404e7c
  * Sunset Orange: #fe5f55
  * Turquoise: #4ce0d2
  * Dark Turqouise: #318f86
  * Sandstorm: #e8d245
  * Soap: #c6caed
  * Fall back for Soap: Silver Sand: #c2c1c2


# PROCESS

**Selecting data from CRCD table**
LEA_STATE,1,text,District State,,
LEA_NAME,2,text,District Name,,
SCH_NAME,3,text,School Name,,
COMBOKEY,4,text,7 Digit LEAID District Identification Code+5 Digit School Identification Code,,
LEAID,5,text,7 Digit LEAID District Identification Code,,
JJ,7,text,"Juvenile Justice Facility: ""Yes"" indicates a long-term secure facility; ""No"" indicates not a JJ facility",,
CCD_LATCOD,8,numeric,CCD: Latitude,,
CCD_LONCOD,9,numeric,CCD: Longitude,,

SCH_ENR_HI_M,62,numeric,Overall Student Enrollment: Hispanic Male,I,7
SCH_ENR_HI_F,63,numeric,Overall Student Enrollment: Hispanic Female,I,7
SCH_ENR_AM_M,64,numeric,Overall Student Enrollment: American Indian/Alaska Native Male,I,7
SCH_ENR_AM_F,65,numeric,Overall Student Enrollment: American Indian/Alaska Native Female,I,7
SCH_ENR_AS_M,66,numeric,Overall Student Enrollment: Asian Male,I,7
SCH_ENR_AS_F,67,numeric,Overall Student Enrollment: Asian Female,I,7
SCH_ENR_HP_M,68,numeric,Overall Student Enrollment: Native Hawaiian/Pacific Islander Male,I,7
SCH_ENR_HP_F,69,numeric,Overall Student Enrollment: Native Hawaiian/Pacific Islander Female,I,7
SCH_ENR_BL_M,70,numeric,Overall Student Enrollment: Black Male,I,7
SCH_ENR_BL_F,71,numeric,Overall Student Enrollment: Black Female,I,7
SCH_ENR_WH_M,72,numeric,Overall Student Enrollment: White Male,I,7
SCH_ENR_WH_F,73,numeric,Overall Student Enrollment: White Female,I,7
SCH_ENR_TR_M,74,numeric,Overall Student Enrollment: Two or More Races Male,I,7
SCH_ENR_TR_F,75,numeric,Overall Student Enrollment: Two or More Races Female,I,7
TOT_ENR_M,76,numeric,Total Number of Students Enrolled: Male,I,7
TOT_ENR_F,77,numeric,Total Number of Students Enrolled: Female,I,7


SCH_GT_IND,215,text,Gifted and Talented Education Program Indicator,I,11
SCH_GTENR_HI_M,216,numeric,Gifted and Talented Students Enrollment: Hispanic Male,I,12
SCH_GTENR_HI_F,217,numeric,Gifted and Talented Students Enrollment: Hispanic Female,I,12
SCH_GTENR_AM_M,218,numeric,Gifted and Talented Students Enrollment: American Indian/Alaska Native Male,I,12
SCH_GTENR_AM_F,219,numeric,Gifted and Talented Students Enrollment: American Indian/Alaska Native Female,I,12
SCH_GTENR_AS_M,220,numeric,Gifted and Talented Students Enrollment: Asian Male,I,12
SCH_GTENR_AS_F,221,numeric,Gifted and Talented Students Enrollment: Asian Female,I,12
SCH_GTENR_HP_M,222,numeric,Gifted and Talented Students Enrollment: Native Hawaiian/Pacific Islander Male,I,12
SCH_GTENR_HP_F,223,numeric,Gifted and Talented Students Enrollment: Native Hawaiian/Pacific Islander Female,I,12
SCH_GTENR_BL_M,224,numeric,Gifted and Talented Students Enrollment: Black Male,I,12
SCH_GTENR_BL_F,225,numeric,Gifted and Talented Students Enrollment: Black Female,I,12
SCH_GTENR_WH_M,226,numeric,Gifted and Talented Students Enrollment: White Male,I,12
SCH_GTENR_WH_F,227,numeric,Gifted and Talented Students Enrollment: White Female,I,12
SCH_GTENR_TR_M,228,numeric,Gifted and Talented Students Enrollment: Two or More Races Male,I,12
SCH_GTENR_TR_F,229,numeric,Gifted and Talented Students Enrollment: Two or More Races Female,I,12
TOT_GTENR_M,230,numeric,Total Number of Students Enrolled in gifted/talented programs: Male,I,12
TOT_GTENR_F,231,numeric,Total Number of Students Enrolled in gifted/talented programs: Female,I,12

SCH_APENR_IND,532,text,Advanced Placement (AP) Program Indicator: Does this school have any students enrolled in Advanced Placement (AP) courses?,i,24
SCH_APCOURSES,533,numeric,Different Advanced Placement (AP) Courses: How many different AP courses does the school provide?,I,25
SCH_APSEL,534,text,Advanced Placement (AP) Course Self-Selection,I,26
SCH_APENR_HI_M,535,numeric,Students Enrolled in at least one AP Course: Hispanic Male,I,27
SCH_APENR_HI_F,536,numeric,Students Enrolled in at least one AP Course: Hispanic Female,I,27
SCH_APENR_AM_M,537,numeric,Students Enrolled in at least one AP Course: American Indian/Alaska Native Male,I,27
SCH_APENR_AM_F,538,numeric,Students Enrolled in at least one AP Course: American Indian/Alaska Native Female,I,27
SCH_APENR_AS_M,539,numeric,Students Enrolled in at least one AP Course: Asian Male,I,27
SCH_APENR_AS_F,540,numeric,Students Enrolled in at least one AP Course: Asian Female,I,27
SCH_APENR_HP_M,541,numeric,Students Enrolled in at least one AP Course: Native Hawaiian/Pacific Islander Male,I,27
SCH_APENR_HP_F,542,numeric,Students Enrolled in at least one AP Course: Native Hawaiian/Pacific Islander Female,I,27
SCH_APENR_BL_M,543,numeric,Students Enrolled in at least one AP Course: Black Male,I,27
SCH_APENR_BL_F,544,numeric,Students Enrolled in at least one AP Course: Black Female,I,27
SCH_APENR_WH_M,545,numeric,Students Enrolled in at least one AP Course: White Male,I,27
SCH_APENR_WH_F,546,numeric,Students Enrolled in at least one AP Course: White Female,I,27
SCH_APENR_TR_M,547,numeric,Students Enrolled in at least one AP Course: Two or More Races Male,I,27
SCH_APENR_TR_F,548,numeric,Students Enrolled in at least one AP Course: Two or More Races Female,I,27
TOT_APENR_M,549,numeric,Total Number of Students Enrolled in at least one AP Course: Male,I,27
TOT_APENR_F,550,numeric,Total Number of Students Enrolled in at least one AP Course: Female,I,27

SCH_FTETEACH_TOT,651,numeric,Teachers - FTE Count and Certification: Total FTE of Teachers,I,50
SCH_FTETEACH_CERT,652,numeric,Teachers - FTE Count and Certification: Number of FTE teachers who are certified,I,50
SCH_FTETEACH_NOTCERT,653,numeric,Teachers - FTE Count and Certification: Number of FTE teachers who are not certified,I,50
SCH_FTETEACH_FY,654,numeric,Teacher Years of Experience: Number of FTE teachers in their first year of teaching,I,51
SCH_FTETEACH_SY,655,numeric,Teacher Years of Experience: Number of FTE teachers in their second year of teaching,I,51
SCH_FTECOUNSELORS,656,numeric,School Counselors: Number of FTE school counselors,I,52
SCH_FTETEACH_ABSENT,657,numeric,Teacher Absenteeism: Number of FTE teachers who were absent more than 10 school days during the school year,II,37
SCH_FTESECURITY_IND,658,text,Sworn Law Enforcement Officers Indicator,I,53

**Preparing selecting the right data**
\d*\W*\bnumeric\S\bGifted and Talented Students Enrollment\S\s\w*\s\w*.* --> replace with nothing
\d*\W*\bnumeric\S\bStudents Enrolled in at least one AP Course\S\s\w*\s\w*.* --> replace with nothing
,\n --> replace with ", "

*gifted and talented*
usecols = ["LEA_STATE", "LEA_NAME", "SCH_NAME", "COMBOKEY", "LEAID", "JJ", "CCD_LATCOD", "CCD_LONCOD", SCH_ENR_HI_M", "SCH_ENR_HI_F", "SCH_ENR_AM_M", "SCH_ENR_AM_F", "SCH_ENR_AS_M", "SCH_ENR_AS_F", "SCH_ENR_HP_M", "SCH_ENR_HP_F", "SCH_ENR_BL_M", "SCH_ENR_BL_F", "SCH_ENR_WH_M", "SCH_ENR_WH_F", "SCH_ENR_TR_M", "SCH_ENR_TR_F", "TOT_ENR_M", "TOT_ENR_F", "SCH_GT_IND", "SCH_GTENR_HI_M", "SCH_GTENR_HI_F", "SCH_GTENR_AM_M", "SCH_GTENR_AM_F", "SCH_GTENR_AS_M", "SCH_GTENR_AS_F", "SCH_GTENR_HP_M", "SCH_GTENR_HP_F", "SCH_GTENR_BL_M", "SCH_GTENR_BL_F", "SCH_GTENR_WH_M", "SCH_GTENR_WH_F", "SCH_GTENR_TR_M", "SCH_GTENR_TR_F", "TOT_GTENR_M", "TOT_GTENR_F", "SCH_GTENR_LEP_M", "SCH_GTENR_LEP_F", "SCH_GTENR_IDEA_M", "SCH_GTENR_IDEA_F"]

- first tried scatter plot -- didn't really look nice, couldn't convey any message
- trying hexbin plots to account for many value counts in a given place
- next trying box plots -- maybe too unfamiliar for people?
- first tries pretty distorted, because many zero values. Setting threshold for data analysed to at least 5% black students in school
--> analysed schools down from 95,000 to roughly 45,000 -- statistic metrices stay almost identical despite downsizing.
 Testing with 2% threshold leaves 60,000 schools in the dataset; similar results
- Histograms of the same thing as a different kind of visualzing the same data

*advanced coursework*
usecols = ["LEA_STATE", "LEA_NAME", "SCH_NAME", "COMBOKEY", "LEAID", "JJ", "CCD_LATCOD", "CCD_LONCOD", SCH_ENR_HI_M", "SCH_ENR_HI_F", "SCH_ENR_AM_M", "SCH_ENR_AM_F", "SCH_ENR_AS_M", "SCH_ENR_AS_F", "SCH_ENR_HP_M", "SCH_ENR_HP_F", "SCH_ENR_BL_M", "SCH_ENR_BL_F", "SCH_ENR_WH_M", "SCH_ENR_WH_F", "SCH_ENR_TR_M", "SCH_ENR_TR_F", "TOT_ENR_M", "TOT_ENR_F", "SCH_APENR_IND", "SCH_APCOURSES", "SCH_APSEL", "SCH_APENR_HI_M", "SCH_APENR_HI_F", "SCH_APENR_AM_M", "SCH_APENR_AM_F", "SCH_APENR_AS_M", "SCH_APENR_AS_F", "SCH_APENR_HP_M", "SCH_APENR_HP_F", "SCH_APENR_BL_M", "SCH_APENR_BL_F", "SCH_APENR_WH_M", "SCH_APENR_WH_F", "SCH_APENR_TR_M", "SCH_APENR_TR_F", "TOT_APENR_M", "TOT_APENR_F"]

- running the same data analysis as for g&t:
  - making a boxplot of the data
  - making a histogram of the data

*counsel vs enforcement*
usecols = ["LEA_STATE", "LEA_NAME", "SCH_NAME", "COMBOKEY", "LEAID", "JJ", "CCD_LATCOD", "CCD_LONCOD", SCH_ENR_HI_M", "SCH_ENR_HI_F", "SCH_ENR_AM_M", "SCH_ENR_AM_F", "SCH_ENR_AS_M", "SCH_ENR_AS_F", "SCH_ENR_HP_M", "SCH_ENR_HP_F", "SCH_ENR_BL_M", "SCH_ENR_BL_F", "SCH_ENR_WH_M", "SCH_ENR_WH_F", "SCH_ENR_TR_M", "SCH_ENR_TR_F", "TOT_ENR_M", "TOT_ENR_F", "SCH_FTETEACH_TOT", "SCH_FTETEACH_CERT", "SCH_FTETEACH_NOTCERT", "SCH_FTETEACH_FY", "SCH_FTETEACH_SY", "SCH_FTECOUNSELORS", "SCH_FTETEACH_ABSENT", "SCH_FTESECURITY_IND"]

- trying a scatter
- trying a hexbin plot
- trying a Histogram
- settling with a slope graph, since everything else looked terrible
- creating a dataframe for that from all the median values
- cleaning & preparing the df for plotting

- choosing median over mean, because it seems to be few high outliers detorting the mean up (seen from a comparatively low third quartile value)

- only looking at law enforcement, in line with the narrative of Georgia's findings of criminalizing
- above that, looking at counselors did not result in the claimed "less likely" (black student population increases by a third when at one counselor is present)
