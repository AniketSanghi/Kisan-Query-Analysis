import csv
import matplotlib.pyplot as plt

month_freq_map = {}
with open('../library/overall_month_frequency.csv') as file:
	for row in csv.DictReader(file):
		year = row["Year"]
		month = row["Month"]
		freq = row["Frequency"]
		if year == "2018" or year == "2020":
			continue
		month_freq_map[int(month)] = int(freq)

month_list = []
frequency_list = []

for month, freq in sorted(month_freq_map.items()):
	month_list.append(str(month))
	frequency_list.append(freq)

plt.plot(month_list, frequency_list, label="2019")

month_freq_map = {}
with open('../library/overall_month_frequency.csv') as file:
	for row in csv.DictReader(file):
		year = row["Year"]
		month = row["Month"]
		freq = row["Frequency"]
		if year == "2018" or year == "2019":
			continue
		month_freq_map[int(month)] = int(freq)

month_list = []
frequency_list = []

for month, freq in sorted(month_freq_map.items()):
	month_list.append(str(month))
	frequency_list.append(freq)

plt.plot(month_list, frequency_list, label="2020")
plt.ylabel("Frequency of Calls")
plt.xlabel("Variation over months/year")
plt.title('Number of calls to KCCs over various months')
plt.legend()
plt.savefig('../images/overall_month_frequency.png')