import json
import csv
import sys

def get_freq_per_state(crop):
    with open("../../data.json", 'r') as f:
        dict = json.load(f)

        crop_freq = {}

        for year, x in dict.items():
            for month, y in x.items():
                for state, z in y.items():
                    for district, w in z.items():
                        for q in w:
                            if state not in crop_freq:
                                crop_freq[state] = 0
                            if q[3] == "Plant Protection" and q[2] == crop:
                                crop_freq[state] += 1

    return crop_freq                            

def output(header, data, filename):
    with open("../data/"+filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(header)  
        csvwriter.writerows(data) 

cropname = sys.argv[1]
crop_freq = get_freq_per_state(cropname)
crop_freq = list(crop_freq.items())
crop_freq.sort(key=lambda  x: x[1], reverse=True)

header = ['State', 'Frequency']
filename = '{}.csv'.format(sys.argv[2])
output(header, crop_freq ,filename)