import json
import re
import csv

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

def output(header, data, filename):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)  
        csvwriter.writerow(header)  
        csvwriter.writerows(data)

with open("../data/relevant_words_queries.json", 'r') as f:
    dict = json.load(f)
    temp = []
    for _, x in dict.items():
        for crop, y in x.items():
            if crop == 'Cotton (Kapas)':
                temp = y
    
    temp = [(x.split('|')[0],x.split('|')[1]) for x in temp]
    temp = [(x[0],int(x[1])) for x in temp]
    temp = unique(temp)
    temp.sort()

    freq = {
        'blight': 0,  # leaf, sheath
        'fly|white': 0,
        'fli|white': 0,
        'insect': 0,
        'suck|pest': 0,
        'thrip': 0, # insect
        'fungal': 0,
        'leaf|curl': 0,
        'flower|drop': 0,
        'boll|worm': 0,
        'ball|worm': 0,
        'ball|warm': 0,
        'boll|warm': 0,
        'dose': 0, # fertilizer/pesticide/weedicide
        'yield': 0,
        'spot': 0, # leaf spot
        'borer': 0, # stem borer, fruit borer
        'wilt': 0,
        'rot': 0, # root
        'yellow': 0, # leaves are yellow
        'reddning': 0, # red leaves
        'red|leaf': 0, # red leaves
        'weed': 0,
        'plant protection': 0,
        'deficiency': 0, # nitrogen, magnesium, zinc, etc.
        'disease': 0, # general
    }
    club = {
        'ball|worm': 'boll|worm',
        'ball|warm': 'boll|worm',
        'boll|warm': 'boll|worm',
        'fli|white': 'fly|white',
        'reddning': 'red|leaf',
    }
    separate = {
        'rot',
        'insect',
        'weed',
    }
    same = {
        'fertilizer': 'dose',
        'pesticide': 'dose',
        'insecticide': 'dose',
        'fungicide': 'dose',
        'weedicide': 'dose',
        'dosage': 'dose',
        'insects': 'insect',
        'termite': 'insect',
        'caterpillar': 'insect', # caterpillar
        'catter': ' insect ', #caterpillar
        'caterpiller': ' insect ', #caterpillar
        'pillar': ' insect ', #caterpillar
        'pilar': ' insect ', #caterpillar
        'piller': ' insect ', #caterpillar
        'aphid': ' insect ',
        'jassid': ' insect ',
        'fungus': 'fungal',
        'fungas': 'fungal',
        'bug': ' insect ',
        'hopper': ' insect ',
        'locust': 'insect',
        'mite': ' insect ',
        'larvae': 'insect',
        'growth': 'yield', # can be increasing or decreasing
        'quality': 'yield',
    }
    separate_same = {
    }

    rem = []
    
    data = temp
    for x,cnt in data:

        for iter in range(2): 
            for a,b in same.items():
                if a in separate_same:
                    x = ' '.join([b if y == a else y for y in x.split()])
                else:
                    x = x.replace(a, b)
                

        flag = 0
        for y in freq:
            if flag == 1:
                break
            ispresent = 1
            for z in y.split('|'):
                temp = x
                if z in separate:
                    temp = x.split()
                if z not in temp:
                    ispresent = 0

            if ispresent == 1:
                freq[y] += cnt
                flag = 1
        
        if 'weather' in x:
            flag = 1
        if flag == 0:
            rem.append((x,cnt))

    ans = []
    cnt = 0
    for x in freq:
        if x in club:
            freq[club[x]]+=freq[x]
    for x, y in freq.items():
        if x in club:
            continue
        ans.append((y,x))
        cnt += y
    ans.sort(reverse=True)
    ans.append([cnt, 'Total'])
    header = ['Count', 'Category']
    output(header, ans, '../data/cotton_data.csv')
    # for x, y in ans:
    #     print(x, y)
    # print('')

    # for x in rem:
    #     print(x[0]+"|"+str(x[1]))
        