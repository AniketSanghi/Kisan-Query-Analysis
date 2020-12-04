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
            if crop == 'Wheat':
                temp = y
    
    temp = [(x.split('|')[0],x.split('|')[1]) for x in temp]
    temp = [(x[0],int(x[1])) for x in temp]
    temp = unique(temp)
    temp.sort()

    freq = {
        'yellow|rust': 0,
        'brown|rust': 0,
        'black|rust': 0,
        'rust': 0,
        'blight': 0,  # leaf, sheath
        'insect': 0,
        'pest': 0,
        'fungal': 0,
        'rat': 0,
        'dose': 0, # fertilizer/pesticide/weedicide
        'yield': 0,
        'borer': 0, # stem borer, shoot borer
        'wilt': 0,
        'rot': 0, # root, stem
        'yellow|leaf': 0, # leaves are yellow
        'yellowing': 0, # leaves are yellow
        'yellowish': 0, # leaves are yellow
        'yellowness': 0, # leaves are yellow
        'yellow': 0,
        'smut': 0, # loose smut
        'time': 0, # irrigation, sowing
        'weed': 0,
        'plant protection': 0,
        'deficiency': 0, # nitrogen, potassium, zinc, etc.
        'disease': 0, # general
        'nutrient': 0, # nutrient management
        'seed treatment': 0,
        'nematode': 0,
    }
    club = {
        'yellowing': 'yellow|leaf',
        'yellowness': 'yellow|leaf',
        'yellowish': 'yellow|leaf',
        'yellow': 'yellow|leaf',
    }
    separate = {
        'rot',
        'insect',
        'weed',
        'rat',
        'time',
    }
    same = {
        'pili': 'yellowing',
        'peel': 'yellowing',
        'peeli': 'yellowing',
        'pilee': 'yellowing',
        'pila': ' yellowing ',
        'fertilizer': 'dose',
        'pesticide': 'dose',
        'insecticide': 'dose',
        'fungicide': 'dose',
        'weedicide': 'dose',
        'dosage': 'dose',
        'insects': ' insect ',
        'termite': ' insect ',
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
        'bunt': 'fungal',
        'hopper': ' insect ',
        'rats': ' rat ',
        'rodent': ' rat ',
        'mouse': ' rat ',
        'weeds': ' weed ',
        'locust': 'insect',
        'worm': 'insect',
        'mite': ' insect ',
        'thrip': ' insect ',
        'larvae': 'insect',
        'kida': 'insect',
        'kide': 'insect',
        'growth': 'yield', # can be increasing or decreasing
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
    output(header, ans, '../data/wheat_data.csv')
    # for x, y in ans:
    #     print(x, y)
    # print('')

    # for x in rem:
    #     print(x[0]+"|"+str(x[1]))
        