from sklearn.feature_extraction.text import TfidfVectorizer
import csv
import json
import numpy as np

with open('../../data/data.json') as file:
	data = json.load(file)

queries = set()
for year, months in data.items():
	for month, states in months.items():
		for state, districts in states.items():
			for district, data_list in districts.items():
				for elem in data_list:
					sector = elem[0]
					category = elem[1]
					crop = elem[2]
					query_type = elem[3]
					query = elem[4]

					queries.add(sector + " " + category + " " + crop + " " + query_type + " " + query)

cnt = 10000
corpus = []
for query in queries:
	if cnt == 0:
		break
	cnt -= 1
	corpus.append(query)

vect = TfidfVectorizer(min_df=1, stop_words="english")                                                                                                                                                                                                   
tfidf = vect.fit_transform(corpus)                                                                                                                                                                                                                       
pairwise_similarity = tfidf * tfidf.T 

n, _ = pairwise_similarity.shape                                                                                                                                                                                                                         
pairwise_similarity[np.arange(n), np.arange(n)] = -1.0

for input_idx in range(0, n):
	maxarg = pairwise_similarity[input_idx].argmax()
	print(corpus[input_idx], "  -->>  ", corpus[maxarg])  