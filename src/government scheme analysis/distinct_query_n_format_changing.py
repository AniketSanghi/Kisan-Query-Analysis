import json

#getting the distinct queries
with open('../data/data.json') as f:
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
with open('./preprocessing/distinct_govt_query', 'w') as f:
    for item in govt_queries:
        f.write("%s\n" % item)
        

with open('./preprocessing/all_govt_query', 'w') as f:
    for item in all_queries:
        f.write("%s\n" % item)

# getting the queire in a particular format
ans_dict = {}
for yr in data_dict:
	ans_dict[yr] = {}
	for month in data_dict[yr]:
		ans_dict[yr][month] = {}
		for state in data_dict[yr][month]:
			ans_dict[yr][month][state] = []
			for dist in data_dict[yr][month][state]:
				temp_list = data_dict[yr][month][state][dist] 
				for elem in temp_list:
					cat = elem[3]
					query = elem[4]
					if (cat=="Government Schemes"):
						ans_dict[yr][month][state].append(query)


with open('./preprocessing/yr_st_gov_sch.json', 'w') as fp:
    json.dump(ans_dict, fp, indent=0)

## making the distinct batches for which translation must be done 

file = open('./preprocessing/distinct_govt_query','r')
Lines = file.read().splitlines()

for i in range(0,24):
	n_lines = Lines[int(i*0.5*10000):int((1+i)*0.5*10000)]
	with open('./preprocessing/batches/temp_translation'+str(i)+'.txt', 'w') as f:
	    for item in n_lines:
	        f.write("%s\n" % item)

n_lines = Lines[int(12.0*10000):-1]
with open('./preprocessing/batches/temp_translation24.txt', 'w') as f:
    for item in n_lines:
        f.write("%s\n" % item)