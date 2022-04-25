
import toolforge
import csv
import pandas as pd

# hoaxes_creation_dates.csv can be found in data/hoaxes
hoaxes_df = pd.read_csv('hoaxes_creation_dates.csv')
hoax_titles = [hoax[10:].replace(' ','_') for hoax in list(hoaxes_df['hoax title'])]
creation_dates = [date.replace('-','') for date in list(hoaxes_df['creation date'])]

conn = toolforge.connect('enwiki_p')
with conn.cursor() as cur:
	cohort_sizes_Xredirects = []
	cohort_sizes_Wredirects = []
	for i in range(len(creation_dates)):
		cur.execute(""" select page_id from revision join page on rev_page = page_id
				where rev_timestamp like %s
				and rev_parent_id = 0
				and page_namespace = 0
				and page_is_redirect = 0;""", (creation_dates[i]+'%',))
		cohort_sizes_Xredirects.append(len(cur.fetchall()))

		cur.execute(""" select page_id from revision join page on rev_page = page_id
				where rev_timestamp like %s
				and rev_parent_id = 0
				and page_namespace = 0;""", (creation_dates[i]+'%',))
		cohort_sizes_Wredirects.append(len(cur.fetchall()))

hoaxes_df['cohort size w/o redirects'] = cohort_sizes_Xredirects
hoaxes_df['cohort size w/ redirects'] = cohort_sizes_Wredirects

# cohort_sizes.csv can be found in data/cohorts
hoaxes_df.to_csv('cohort_sizes.csv')
