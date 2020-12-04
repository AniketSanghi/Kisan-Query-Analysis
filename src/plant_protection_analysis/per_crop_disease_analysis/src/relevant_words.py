import json
import re
from extract_keywords import *

def unique(z):
    freq = {}
    for x in z:
        if x[0] not in freq:
            freq[x[0]] = 0
        freq[x[0]] += x[1]
    
    ans = []
    for x, y in freq.items():
        ans.append((x,y))
    return ans

data_dir = '../../../data/'
with open("{}data.json".format(data_dir), 'r') as f:
    dict = json.load(f)

    queries = {}
    for year, x in dict.items():
        for month, y in x.items():
            for state, z in y.items():
                for district, w in z.items():
                    for q in w:

                        key = q[3]
                        if key != "Plant Protection":
                            continue
                        
                        if key not in queries:
                            queries[key] = {}
                        if q[2] not in queries[key]:
                            queries[key][q[2]] = []
                        queries[key][q[2]].append(q[4])

    cnt = 0
    data = {}
    for x,y in queries.items():
        data[x] = {}
        for y,z in queries[x].items():

            if len(z) <= 20000:
                continue

            z = [(x,1) for x in z]
            z = unique(z)
            z.sort()
            z = [((x[0], filter_sentence(x[0])), x[1]) for x in z]
            z = [x for x in z if x[0][1]!='']

            z = [(x[0][1],x[1]) for x in z]
            z = unique(z)
            z.sort()
            data[x][y] = [x[0]+"|"+str(x[1]) for x in z]

    with open('../data/relevant_words_queries.json', 'w', encoding='utf8') as outfile:
        outfile.write(json.dumps(data, sort_keys=True, indent=0, ensure_ascii=False))