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
            if crop == 'Paddy (Dhan)':
                temp = y
    
    temp = [(x.split('|')[0],x.split('|')[1]) for x in temp]
    temp = [(x[0],int(x[1])) for x in temp]
    temp = unique(temp)
    temp.sort()

    freq = {
        'blight': 0,  # leaf, sheath
        'rot': 0, # sheath, foot, root, leaf, stem
        'yellow': 0, # leaves are yellow
        'borer': 0, # stem borer, root borer
        'dose': 0, # fertilizer/pesticide/weedicide
        'insect': 0,
        'blast': 0,
        'smut': 0, # false smut, kernel smut
        'fungal': 0,
        'scald': 0, # leaf scald
        'khaira': 0,
        'haldia': 0,
        'weed': 0,
        'spot': 0, # leaf, black, brown spot
        'baka': 0, # bakanae disease
        'dry': 0,
        'plant protection': 0,
        'deficiency': 0, # iron, potassium, zinc, etc.
        'disease': 0, # general
        'yield': 0,
        'nutrient': 0, # nutrient management
        'seed treatment': 0,
        'cold injur': 0,
        'nematode': 0,
        'leaf|white': 0,
    }
    separate = {
        'rot',
        'insect',
        'weed',
    }
    same = {
        'pili': 'yellow',
        'peel': 'yellow',
        'peeli': 'yellow',
        'pilee': 'yellow',
        'fertilizer': 'dose',
        'pesticide': 'dose',
        'insecticide': 'dose',
        'fungicide': 'dose',
        'weedicide': 'dose',
        'dosage': 'dose',
        'insects': 'insect',
        'termite': 'insect',
        'caterpillar': 'insect',
        'aphid': 'insect',
        'grasshopper': 'insect',
        'hopper': 'insect',
        'planthopper': 'insect',
        'leafhopper': 'insect',
        'tidda': 'insect',
        'pest': 'insect',
        'pests': 'insect',
        'deemak': 'insect',
        'bug': ' insect ', # earhead, gundhi
        'moth': ' insect ', # earhead, gundhi
        'whitefl': ' insect ',
        'white fl': ' insect ',
        'gall midge': ' insect ',
        'folder': ' insect ', # leaf folder
        'roller': ' insect ', # leaf folder/roller
        'bph': ' insect ', # brown plant hopper
        'hispa': 'insect',
        'locust': 'insect',
        'leafinsect': 'insect',
        'worm': 'insect',
        'mite': 'insect',
        'thrip': 'insect',
        'larvae': 'insect',
        'kida': 'insect',
        'kide': 'insect',
        'jhoka': 'blast',
        'jhonka': 'blast',
        'jhulsa': 'blast',
        'algae': 'fungal',
        'algal': 'fungal',
        'algee': 'fungal',
        'fungi': 'fungal',
        'fungus': 'fungal',
        'fungas': 'fungal',
        'shoot': 'stem',
        'sukh': 'dry',
        'wilt': 'dry',
        'weeds': 'weed',
        'growth': 'yield',
        'safed': 'leaf white',
        'boror': 'borer',
        'blb': 'blight' # bacterial blight
    }
    separate_same = {
        'pili',
        'peel',
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
    for x, y in freq.items():
        ans.append((y,x))
        cnt += y
    ans.sort(reverse=True)
    ans.append([cnt, 'Total'])
    header = ['Count', 'Category']
    output(header, ans, '../data/paddy_data.csv')
    # for x, y in ans:
        # print(x, y)
    # print('')

    # for x in rem:
        # print(x[0]+"|"+str(x[1]))
        