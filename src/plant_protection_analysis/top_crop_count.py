import json

with open("data.json", 'r') as f:
    dict = json.load(f)
    temp = {}
    for year, x in dict.items():
        for month, y in x.items():
            for state, z in y.items():
                for district, w in z.items():
                    for q in w:
                        key = q[3]
                        if key != "Plant Protection":
                            continue

                        if q[2] not in temp:
                            temp[q[2]] = []
                        temp[q[2]].append(q[4])

    cnt = []
    for x, y in temp.items():
        cnt.append((len(y), x))
    cnt.sort(reverse=True)

    count = 0
    for x, y in cnt:
        if x > 20000:
            print(y, x)
            count += x
    print(count)
    