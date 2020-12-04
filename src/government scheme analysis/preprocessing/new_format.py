import json

with open('./data.json') as f:
  data_dict = json.load(f)


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


with open('yr_st_gov_sch.json', 'w') as fp:
    json.dump(ans_dict, fp, indent=0)