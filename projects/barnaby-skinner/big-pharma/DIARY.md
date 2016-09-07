# Data Dairy for Pharma

## DOCUMENTATION of cleaning process

-> Import und concat with Python
-> Export .csv for Open Refine
	-> First cleaning (dealing with dates, that should be ints
	-> Checking the difficult files, Bayer, Novartis, Takeda
	-> Clustering cities (La Chaux-de-Fonds, Gross-Kleinschreibung, etc.)
	-> Clustering hospitals and clinics
  -> Clustering hospitals further (new column)
    -> What to do with foundations that are attached to Universities?
		Where it is clear, I have decided to include them.
		-> Cluster all the Uni-Spitäler and Kantonsspitäler Addresses

## QUERYING the data

-> Import back into Pandas
-> What is with the total values?
-> Establish cantons of institutions
-> Double check with Beo/SRF figures
-> Plot: 20 institutions with most payments
-> Plot: How do top hospitals compare?
Universitätsspital Basel (USB)
Inselspital Bern
Hôpitaux Universitaires de Genève HUG
Hospices/CHUV Lausanne
Universitätsspital Zürich
Including these hospitals:
http://www.gastromed.ch/spitalliste.html

## This function won't work, and I don't understand why
It is supposed to remove " ' " from the columns, but it returns nones.

def find(x):
    pattern = re.compile(r"'")
    try:
        if pattern.findall(x):
            x = x.replace("'", "")
            return x
    except:
        return x
