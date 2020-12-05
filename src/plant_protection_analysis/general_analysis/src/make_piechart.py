import matplotlib.pyplot as plt 
import sys
import csv

filename = "../data/"+sys.argv[1]+".csv"

crops = []
data = []
total = 0

with open(filename, 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    next(csvreader)

    for row in csvreader:
        crop = row[0]
        crop = crop.split('(')[0].strip()
        freq = int(row[1])

        if crop == 'Total':
            total = freq
            break

        data.append(freq)
        crops.append(crop)
        
length = len(crops)
for i in range(len(crops)):
    perc = (100*data[i])//total
    if perc < 3:
        length = i
        break
    data[i] = perc

data = data[:length]
crops = crops[:length]

data.append(100-sum(data))
crops.append('Others')

fig1, ax1 = plt.subplots(figsize=(8, 7))
fig1.subplots_adjust(0.3,0,1,1)

wp = { 'linewidth' : 1, 'edgecolor' : "green" } 
_, _ = ax1.pie(data, startangle=90, wedgeprops=wp, shadow=True)

ax1.axis('equal')

total = sum(data)
plt.legend(
    loc='upper left',
    labels=[l + ", " + str(s) + "%" for l, s in zip(crops, data)],
    prop={'size': 11},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig1.transFigure,
    title="Percentage of Crop"
)
  
dest = "../plots/"+sys.argv[1]+".png"
plt.savefig(dest)

plt.close()
