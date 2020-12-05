import matplotlib.pyplot as plt 
import sys
import csv

filename = "../library/overall_crop_frequency.csv"

crops = []
data = []
total = 0
others = 0

with open(filename, 'r') as csvfile:
    for line in csv.DictReader(csvfile):
        crop = line["Crop"]
        freq = int(line["Frequency"])

        if crop == 'Total':
            total = freq
            continue

        if crop == 'Others' or crop == 'NA':
            others += freq
            continue

        data.append(freq)
        crops.append(crop)
        
total -= others
length = len(crops)
for i in range(len(crops)):
    perc = (100*data[i])//total
    if perc < 2:
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
  
dest = "../images/overall_crops_frequency.png"
plt.savefig(dest)

plt.close()