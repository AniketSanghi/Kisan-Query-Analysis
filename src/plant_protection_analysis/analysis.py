import json
import re
from extract_keywords import *

def output(temp):
    # temp = list(temp.keys())
    # temp.sort()
    # mappings = {
    #     172: ' ',
    #     174: ' ',
    #     176: ' ',
    #     183: ' ',
    #     186: ' ',
    #     8211: ' ',
    #     8212: ' ',
    #     8216: '\'',
    #     8217: '\'',
    #     8220: '"',
    #     8221: '"',
    #     8226: ' ',
    #     8230: '.',
    #     8482: ' ',
    # }
    keys = list(temp.keys())
    keys.sort()
    for x in keys:
        print(x)
    print("_____________")
    # count = 0
    # # patterns = ['\d+/\d+/\d+[a-z]', '°']
    # # english_patters = ['^ask', '^yellow', '^white', '^weather', '^information', '^farmer', '^about', '^fertilizer', '^control', '^please', '^regarding']
    # freq = {}
    # for x in keys:
    #     cnt = sum(ch.isalpha() for ch in x)
    #     if len(x)>0 and cnt/len(x)>=0.6:
    #         # if not all(c.isalpha() or c.isspace() for c in x):
    #         if not re.search('|'.join(patterns), x):
    #             # firstword = x.split()[0]
    #             # if firstword not in freq:
    #             #     freq[firstword] = 0
    #             # freq[firstword] += 1 
    #             if re.search('|'.join(english_patters), x):
    #                 count += 1
    # print(count)
    # for x,y in freq.items():
    #     if y>100:
    #         print(x,y)
                # print(x, temp[x])
    # for x in temp:
    #     if not x.isascii():
    #         for p, q in mappings.items():
    #             x = x.replace(chr(p), q)
    #     print(x)
        #     if not x.isascii():
        #         print(x)
    # print("_____________")

with open("data.json", 'r') as f:
    dict = json.load(f)
    cnt = 0
    total = 0
    temp = {}
    # years, months, states, districts = {}, {}, {}, {}
    # sector, category, crop, query_type = {}, {}, {}, {}
    for year, x in dict.items():
        # years[year] = 1
        for month, y in x.items():
            # months[month] = 1
            for state, z in y.items():
                # states[state] = 1
                for district, w in z.items():
                    # districts[district] = 1
                    # cnt += len(w)
                    for q in w:
                        # if q[4] not in temp:
                        #     temp[q[4]] = 0
                        total += 1
                        key = q[3]
                        if key != "Plant Protection":
                            continue
                        cnt += 1
                        # if key not in temp:
                        #     temp[key] = {}
                        # if q[2] not in temp[key]:
                        #     temp[key][q[2]] = []
                        # temp[key][q[2]].append(q[4])
                        # temp[q[4]] = 1
                        # sector[q[0]] = 1
                        # category[q[1]] = 1
                        # crop[q[2]] = 1
                        # query_type[q[3]] = 1
                        # if re.search(r"\b" + "call" + r"\b", q[4], re.IGNORECASE):
                        # if len(q[4]) > 150:
                        #     temp1[q[4]] = 1
                        # cnt += 1
    print(cnt, total)
    # output(temp)
    # for x,y in temp.items():
    #     for y,z in temp[x].items():
    #         z = list(set(z))
    #         z.sort()
    #         temp[x][y] = z
    #         # features = get_top_features(y, 10000)
    # # for x in features:
    # #     print(x)
    # with open('query_type_crop_query.json', 'w', encoding='utf8') as outfile:
    #     outfile.write(json.dumps(temp, sort_keys=True, indent=0, ensure_ascii=False))
    # output(years)
    # output(months)
    # output(states)
    # output(districts)
    # output(sector)
    # output(category)
    # output(crop)
    # output(query_type)