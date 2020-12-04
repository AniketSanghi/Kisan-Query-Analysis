import sys

with open(sys.argv[1], 'r') as f:

    freq = {}
    for x in f.readlines():
        x = x.strip()

        if len(x)==0 or x[0].isdigit():
            continue
        x, cnt = x.split('|')[0], x.split('|')[1]
        freq[x] = cnt
        
    ans = []
    cnt = 0
    for x,y in freq.items():
        cnt += int(y)
        ans.append((int(y),x))
    ans.sort(reverse=True)
    print(cnt)
    for x in ans:
        print(x)        