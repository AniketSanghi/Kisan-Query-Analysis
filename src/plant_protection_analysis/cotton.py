import json
import re
from extract_keywords import *
from cluster import *

mappings = {
    'dhaan':'paddy',
    'dhan': 'paddy',
    'dhann': 'paddy',
    'rice': 'paddy'
}
def replace(sent):
    # sent = [mappings.get(w, w) for w in sent.split()]
    # sent = ' '.join(sent)
    return sent
    
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

with open("query_type_crop_query_relevant_words_distinct_threshold.json", 'r') as f:
    dict = json.load(f)
    # cnt = 0
    temp = []
    for _, x in dict.items():
        for crop, y in x.items():
            if crop == 'Cotton (Kapas)':
                temp = y
    
    temp = [(x.split('|')[0],x.split('|')[1]) for x in temp]
    temp = [(replace(x[0]),int(x[1])) for x in temp]
    # temp = list(set(temp))
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
        # 'blast': 0,
        # 'smut': 0, # false smut, kernel smut
        # 'scald': 0, # leaf scald
        # 'khaira': 0,
        # 'haldia': 0,
        'weed': 0,
        # 'baka': 0, # bakanae disease
        # 'dry': 0,
        'plant protection': 0,
        'deficiency': 0, # nitrogen, magnesium, zinc, etc.
        'disease': 0, # general
        # 'nutrient': 0, # nutrient management
        # 'seed treatment': 0,
        # 'cold injur': 0,
        # 'nematode': 0,
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
        # 'pili': 'yellow',
        # 'peel': 'yellow',
        # 'peeli': 'yellow',
        # 'pilee': 'yellow',
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
        # 'planthopper': 'insect',
        # 'leafhopper': 'insect',
        # 'tidda': 'insect',
        # 'pest': 'insect',
        # 'pests': 'insect',
        # 'deemak': 'insect',
        # 'bug': ' insect ', # earhead, gundhi
        # 'moth': ' insect ', # earhead, gundhi
        # 'whitefl': ' insect ',
        # 'white fl': ' insect ',
        # 'gall midge': ' insect ',
        # 'folder': ' insect ', # leaf folder
        # 'roller': ' insect ', # leaf folder/roller
        # 'bph': ' insect ', # brown plant hopper
        # 'hispa': 'insect',
        'locust': 'insect',
        # 'leafinsect': 'insect',
        # 'worm': 'insect',
        'mite': ' insect ',
        # 'thrip': 'insect',
        'larvae': 'insect',
        # 'kida': 'insect',
        # 'kide': 'insect',
        # 'jhoka': 'blast',
        # 'jhonka': 'blast',
        # 'jhulsa': 'blast',
        # 'algae': 'fungal',
        # 'algal': 'fungal',
        # 'algee': 'fungal',
        # 'fungi': 'fungal',
        # 'shoot': 'stem',
        # 'sukh': 'dry',
        # 'wilt': 'dry',
        # 'weeds': 'weed',
        'growth': 'yield', # can be increasing or decreasing
        'quality': 'yield',
        # 'safed': 'leaf white',
        # 'boror': 'borer',
        # 'blb': 'blight' # bacterial blight
    }
    separate_same = {
        # 'pili',
        # 'peel',
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
    bla = 0
    for x in freq:
        if x in club:
            freq[club[x]]+=freq[x]
    for x, y in freq.items():
        if x in club:
            continue
        ans.append((y,x))
        bla += y
    print(bla)
    ans.sort(reverse=True)
    for x, y in ans:
        print(x, y)
    print('')

    for x in rem:
        print(x[0]+"|"+str(x[1]))
        