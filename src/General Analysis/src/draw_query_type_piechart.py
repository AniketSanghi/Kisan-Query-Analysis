import matplotlib.pyplot as plt 
import sys
import csv

filename = "../library/overall_query_type_frequency.csv"

query_types = []
data = []
total = 0

with open(filename, 'r') as csvfile:
    for line in csv.DictReader(csvfile):
        query_type = line["QueryType"]
        freq = int(line["Frequency"])

        if query_type == 'Total':
            total = freq
            continue

        data.append(freq)
        query_types.append(query_type)
        
length = len(query_types)
for i in range(len(query_types)):
    perc = (100*data[i])//total
    if perc < 3:
        length = i
        break
    data[i] = perc

data = data[:length]
query_types = query_types[:length]

data.append(100-sum(data))
query_types.append('Others')

fig1, ax1 = plt.subplots(figsize=(8, 7))
fig1.subplots_adjust(0.3,0,1,1)

wp = { 'linewidth' : 1, 'edgecolor' : "green" } 
_, _ = ax1.pie(data, startangle=90, wedgeprops=wp, shadow=True)

ax1.axis('equal')

total = sum(data)
plt.legend(
    loc='upper left',
    labels=[l + ", " + str(s) + "%" for l, s in zip(query_types, data)],
    prop={'size': 11},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig1.transFigure,
    title="Percentage of Crop"
)
  
dest = "../images/overall_query_types_frequency.png"
plt.savefig(dest)

plt.close()