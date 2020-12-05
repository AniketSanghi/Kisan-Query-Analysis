import matplotlib.pyplot as plt 
import sys
import csv

filename = "../data/"+sys.argv[1]+".csv"

categories = []
data = {}
total = 0

mappings = {}

threshold = 0

if sys.argv[1] == 'paddy_data':
    mappings = {
        'nematode': 'insect'
    }
    threshold = 3

elif sys.argv[1] == 'cotton_data':
    mappings = {
        'suck|pest': 'insect',
        'fly|white': 'white flies',
        'boll|worm': 'insect',
        'flower|drop': 'flower dropping',
        'borer': 'insect',
        'thrip': 'insect',
    }
    threshold = 2

elif sys.argv[1] == 'wheat_data':
    mappings = {
        'nematode': 'insect',
        'pest': 'insect',
        'borer': 'insect',
        'yellow|rust': 'yellow rust',
        'yellow|leaf': 'yellow leaves'
    }
    threshold = 3

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        freq = int(row[0])
        category = mappings.get(row[1], row[1])

        if category == 'Total':
            total = freq
            break

        if category not in data:
            data[category] = 0

        data[category] += freq

temp = list(data.items())
temp.sort(key=lambda x: x[1], reverse=True)
categories = [x[0] for x in temp]
data = [x[1] for x in temp]

length = len(categories)
for i in range(len(categories)):
    perc = (100*data[i])//total
    if perc < threshold:
        length = i
        break
    data[i] = perc

data = data[:length]
categories = categories[:length]

data.append(100-sum(data))
categories.append('Others')

fig1, ax1 = plt.subplots(figsize=(8, 7))
fig1.subplots_adjust(0.3,0,1,1)

wp = { 'linewidth' : 1, 'edgecolor' : "green" } 
_, _ = ax1.pie(data, startangle=90, wedgeprops=wp, shadow=True)

ax1.axis('equal')

total = sum(data)
plt.legend(
    loc='upper left',
    labels=[l + ", " + str(s) + "%" for l, s in zip(categories, data)],
    prop={'size': 11},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig1.transFigure,
    title="Percentage of category"
)
  
dest = "../plots/"+sys.argv[1]+".png"
plt.savefig(dest)

plt.close()
