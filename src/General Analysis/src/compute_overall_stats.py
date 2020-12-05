import csv
import json

with open('../../data/data.json') as file:
	data = json.load(file)

year_month_frequency = {}
state_frequency = {}
district_frequency = {}
crop_frequency = {}
total_queries = 0
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

					if district in district_frequency.keys():
						district_frequency[district] += 1
					else:
						district_frequency[district] = 1

					crop = data_elem[2]
					if crop in crop_frequency.keys():
						crop_frequency[crop] += 1
					else:
						crop_frequency[crop] = 1

					total_queries += 1


with open('../library/overall_month_frequency.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Year", "Month", "Frequency"])
	for year_month, freq in year_month_frequency.items():
		writer.writerow([year_month.split('/')[0], year_month.split('/')[1], freq])

with open('../library/overall_state_frequency.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["State", "Frequency"])
	for state, freq in sorted(state_frequency.items(), key=lambda x: x[1], reverse=True):
		writer.writerow([state, freq])

with open('../library/overall_district_frequency.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["District", "Frequency"])
	for district, freq in sorted(district_frequency.items(), key=lambda x: x[1], reverse=True):
		writer.writerow([district, freq])

with open('../library/overall_crop_frequency.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Crop", "Frequency"])
	writer.writerow(["Total", total_queries])
	for crop, freq in sorted(crop_frequency.items(), key=lambda x: x[1], reverse=True):
		writer.writerow([crop, freq])