import csv
import json

with open('../../data/data.json') as file:
	data = json.load(file)

year_month_frequency = {}
state_frequency = {}
for year, months in data.items():
	for month, states in months.items():
		for state, districts in states.items():
			for district, data_list in districts.items():
				for data_elem in data_list:
					year_month = year + "/" + month
					if year_month in year_month_frequency.keys():
						year_month_frequency[year_month] += 1
					else:
						year_month_frequency[year_month] = 1

					if state in state_frequency.keys():
						state_frequency[state] += 1
					else:
						state_frequency[state] = 1


with open('../library/overall_month_frequency.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Year", "Month", "Frequency"])
	for year_month, freq in year_month_frequency.items():
		writer.writerow([year_month.split('/')[0], year_month.split('/')[1], freq])

with open('../library/overall_state_frequency.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["State", "Frequency"])
	for state, freq in state_frequency.items():
		writer.writerow([state, freq])