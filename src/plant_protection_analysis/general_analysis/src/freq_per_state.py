import json
import csv
import sys

data_dir = '../../../data/'
def get_freq_per_state():
    with open("{}data.json".format(data_dir), 'r') as f:
        dict = json.load(f)

        freq = {}

        for year, x in dict.items():
            for month, y in x.items():
                for state, z in y.items():
                    for district, w in z.items():
                        for q in w:
                            if state not in freq:
                                freq[state] = 0
                            if q[3] == "Plant Protection":
                                freq[state] += 1

    return freq                            

def output(header, data, filename):
    with open("../data/"+filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(header)  
        csvwriter.writerows(data) 

freq = get_freq_per_state()
freq = list(freq.items())
freq.sort(key=lambda  x: x[1], reverse=True)

header = ['State', 'Frequency']
filename = '{}.csv'.format(sys.argv[1])
output(header, freq ,filename)