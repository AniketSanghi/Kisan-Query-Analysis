import json
import csv
import sys

data_dir = '../../../data/'
def get_freq_per_month(crop):
    with open("{}data.json".format(data_dir), 'r') as f:
        dict = json.load(f)

        crop_freq = {}
        for year, x in dict.items():
            for month, y in x.items():
                for state, z in y.items():
                    for district, w in z.items():
                        for q in w:
                            key = (int(year), int(month))
                            if key not in crop_freq:
                                crop_freq[key] = 0

                            if q[3] == "Plant Protection" and q[2] == crop:
                                crop_freq[key] += 1

    return crop_freq                            

def output(header, data, filename):
    with open("../data/"+filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(header)  
        csvwriter.writerows(data) 

cropname = sys.argv[1]
crop_freq = get_freq_per_month(cropname)
crop_freq = list(crop_freq.items())
crop_freq.sort(key=lambda  x: x[0], reverse=False)
crop_freq = [(str(x[0][0])+"|"+str(x[0][1]),x[1]) for x in crop_freq]

header = ['Month', 'Frequency']
filename = '{}.csv'.format(sys.argv[2])
output(header, crop_freq ,filename)