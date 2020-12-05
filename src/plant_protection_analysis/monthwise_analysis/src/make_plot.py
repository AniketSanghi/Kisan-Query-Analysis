import sys
import csv
import matplotlib.pyplot as plt 

filename = "../data/"+sys.argv[1]+".csv"
month_list = [10,11,12,1,2,3,4,5,6,7,8,9]
freq_list1 = {}
freq_list2 = {}

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        year, month = int(row[0].split('|')[0]), int(row[0].split('|')[1])
        freq = int(row[1])

        if year == 2018 or (year == 2019 and month < 10):
            freq_list1[month] = freq
        else:
            freq_list2[month] = freq

freq_list1 = [freq_list1.get(x, 0) for x in month_list]
freq_list2 = [freq_list2.get(x, 0) for x in month_list]

dummy_list = [x for x in range(12)]
plt.plot(dummy_list, freq_list1, label="2018 Oct - 2019 Sept")
plt.plot(dummy_list, freq_list2, label="2019 Oct - 2020 Sept")


plt.xticks(dummy_list, month_list)

plt.ylabel("Frequency of Calls")
plt.xlabel("Variation over months/year")
plt.title('Number of calls to KCCs over various months for Plant Protection in {}'.format(sys.argv[2]))
plt.legend()

dest = "../plots/"+sys.argv[1]+".png"
plt.savefig(dest)

plt.close()
