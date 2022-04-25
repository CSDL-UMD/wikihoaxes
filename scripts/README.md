# Quering Wikimedia databases
The scipts run mysql queries against the replica databases.

## cohort_sizes.py
1. connects the enwiki replica database
2. extracts the number of cohort members for each hoax with and without redirects

## extract_cohort.py
1. extracts the page IDs of all cohort members for each respective hoax

## get_neighbors.py
1. fetchs the outlinks of each hoax in the dataset
2. fetchs the outlinks for each hoax's cohort

## cohort_dict.p
1. pickle file containing cohort information needed to run get_neighbors
2. it can be found in data/cohorts within the data's drive folder link

## hoaxes_creation_dates.csv
1. csv file containing the creation dates of hoaxes need to run extract_cohort.py and get_neighbors.py
2. it can be found in data/hoaxes in the data's drive folder link.

#### Toolforge python library
To be able to run the scripts and access the databases within Toolforge, toolforge library is needed.
For python's toolforge documentation, visit the link:
https://wikitech.wikimedia.org/wiki/User:Legoktm/toolforge_library
