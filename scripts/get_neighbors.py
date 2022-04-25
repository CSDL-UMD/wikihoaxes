import toolforge
import pickle

# temporary for getting neighbors for the cohort
# the file 'cohort_dict(parsing_pagecounts.ipynb).p' can be found in data/cohorts
cohort_dict = pickle.load(open('cohort_dict.p', 'rb'))

def get_neighbors():
    conn = toolforge.connect('enwiki_p')
    hoax_neighbors = {}
    nonhoax_neighbors = {}
    with conn.cursor() as cur:
        for key, value in cohort_dict.items():
            # getting hoaxes outlinks
            cur.execute(""" select page_title
                            from pagelinks join page
                            on pl_title = page_title
                            where pl_from = %s 
                            and pl_from_namespace = 4 
                            and pl_namespace = 0
                            and page_namespace = 0; """,(value['hoax_id'],))
            hoax_neighbors[str(value['hoax_id'])] = {'outlinks': [row[0] for row in cur.fetchall()]}

            for nonhoax in value['nonhoax_id']:
                # getting nonhoaxes outlinks
                cur.execute(""" select page_title
                                from pagelinks join page
                                on pl_title = page_title
                                where pl_from = %s 
                                and pl_from_namespace = 0 
                                and pl_namespace = 0
                                and page_namespace = 0; """,(nonhoax,))
                nonhoax_neighbors[str(nonhoax)].update({'outlinks': [row[0] for row in cur.fetchall()]})

        return hoax_neighbors, nonhoax_neighbors

hoax_neighbors, nonhoax_neighbors = get_neighbors()

# The following two pickle files are saved in data/topics(neighbors)
pickle.dump(hoax_neighbors, open('hoax_neighbors.p', 'wb'), pickle.HIGHEST_PROTOCOL)
pickle.dump(nonhoax_neighbors, open('cohort_neighbors.p', 'wb', pickle.HIGHEST_PROTOCOL))
