import json

with open('../data.json') as f:
  data_dict = json.load(f)


govt_queries = []
all_queries = []
dummy_set = {""}
for yr in data_dict:
	for month in data_dict[yr]:
		for state in data_dict[yr][month]:
			for dist in data_dict[yr][month][state]:
				temp_list = data_dict[yr][month][state][dist]
				for elem in temp_list:
					cat = elem[3]
					query = elem[4]
					if (cat=="Government Schemes"):
						all_queries.append(query)
						if(query not in dummy_set):
							govt_queries.append(query)
							dummy_set.add(query)


govt_queries.sort()
with open('distinct_govt_query', 'w') as f:
    for item in govt_queries:
        f.write("%s\n" % item)
        

with open('all_govt_query', 'w') as f:
    for item in all_queries:
        f.write("%s\n" % item)