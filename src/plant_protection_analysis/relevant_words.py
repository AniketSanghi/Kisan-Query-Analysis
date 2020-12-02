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

with open("data.json", 'r') as f:
    dict = json.load(f)
    # cnt = 0
    temp = {}
    distinct = {}
    for year, x in dict.items():
        for month, y in x.items():
            for state, z in y.items():
                for district, w in z.items():
                    for q in w:
                        # if q[4] not in temp:
                        #     temp[q[4]] = 0
                        key = q[3]
                        if key != "Plant Protection":
                            continue
                        
                        # distinct[q[4]] = 1

                        if key not in temp:
                            temp[key] = {}
                        if q[2] not in temp[key]:
                            temp[key][q[2]] = []
                        temp[key][q[2]].append(q[4])

    # print(cnt)
    # output(temp)
    cnt = 0
    data = {}
    for x,y in temp.items():
        data[x] = {}
        for y,z in temp[x].items():
            # cnt[y] = len(z)
            # cnt += len(z)
            if len(z) <= 20000:
                # del temp[x][y]
                continue
            # z = list(set(z))
            z = [(x,1) for x in z]
            z = unique(z)
            z.sort()
            z = [((x[0], filter_sentence(x[0])), x[1]) for x in z]
            z = [x for x in z if x[0][1]!='']

            z = [(x[0][1],x[1]) for x in z]
            # z = list(set(z))
            z = unique(z)
            z.sort()
            # for w in z:
            #     # words.update(w[1].split())
            #     mispelled = spell.unknown(w.split())
            #     for word in mispelled:
            #         if word not in spellings:
            #             spellings[word] = spell.correction(word)
            # temp[x][y] = z
            data[x][y] = [x[0]+"|"+str(x[1]) for x in z]

            # cnt += 1
            # print(cnt)
            # features = get_top_features(y, 10000)
    # keys = list(cnt.keys())
    # keys.sort()
    # for x in keys:
    #     print(x, cnt[x])
    # print(cnt)
    # # for x in features:
    # #     print(x)
    # words = list(words)
    # words.sort()
    # for x in words:
    #     print(x)
    # spellings_keys = list(spellings.keys())
    # spellings_keys.sort()
    # for x in spellings_keys:
    #     print(x, spellings_keys[x])
    with open('query_type_crop_query_relevant_words_distinct_threshold.json', 'w', encoding='utf8') as outfile:
        outfile.write(json.dumps(data, sort_keys=True, indent=0, ensure_ascii=False))