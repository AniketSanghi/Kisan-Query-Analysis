import csv
import json

with open('../../data/data.json') as file:
	data = json.load(file)

top_query_types = ["Weather", "Plant Protection", "Government Schemes", "Nutrient Management"]

query_type_query = {}
total = 0
queryType_state_frequency = {}
for year, months in data.items():
	for month, states in months.items():
		for state, districts in states.items():
			for district, data_list in districts.items():
				for data_elem in data_list:
					total += 1
					queryType = data_elem[3]
					if data_elem[3] in query_type_query.keys():
						query_type_query[queryType].append(data_elem[4])
					else:
						query_type_query[queryType] = [data_elem[4]]

					if queryType in queryType_state_frequency.keys():
						if state in queryType_state_frequency[queryType].keys():
							queryType_state_frequency[queryType][state] += 1
						else:
							queryType_state_frequency[queryType][state] = 1
					else:
						queryType_state_frequency[queryType] = {state: 1}

frequency_sorted_queryTypes = []

with open("../library/query_type_frequency.csv", 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["QueryType", "Frequency"])
	writer.writerow(["Total", total])
	for query_type, queries in sorted(query_type_query.items(), key=lambda x:len(x[1]), reverse=True):
		writer.writerow([query_type, len(queries)])
		frequency_sorted_queryTypes.append(query_type)

for i in range(4, len(frequency_sorted_queryTypes)):
	query_type = frequency_sorted_queryTypes[i]
	del queryType_state_frequency[query_type]

for queryType, states in queryType_state_frequency.items():
	with open("../library/category/" + '_'.join(queryType.split(' ')) + "_state_frequency.csv", 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(["State", "Frequency"])
		for state, frequency in states.items():
			writer.writerow([state, frequency])