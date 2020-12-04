import json
import csv

def output(header, data, filename):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(header)  
        csvwriter.writerows(data) 

data_dir = '../../../data/'
with open("{}data.json".format(data_dir), 'r') as f:
    dict = json.load(f)
    crops = {}
    for year, x in dict.items():
        for month, y in x.items():
            for state, z in y.items():
                for district, w in z.items():
                    for q in w:
                        key = q[3]
                        if key != "Plant Protection":
                            continue

                        if q[2] not in crops:
                            crops[q[2]] = []
                        crops[q[2]].append(q[4])

    cnt = []
    for x, y in crops.items():
        cnt.append((len(y), x))
    cnt.sort(reverse=True)

    count = 0
    data = []
    for x, y in cnt:
        if x > 10000:
            data.append([y, x])
            count += x

    data.append(['Total', count])
    header = ['Crop', 'Count']
    output(header, data, '../data/top_crop_count.csv')
