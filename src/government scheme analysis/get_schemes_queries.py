import json
import csv

with open('preprocessing/yr_st_gov_sch.json') as f:
    st_query = json.load(f)

state_list = {}
for yr in st_query:
    for month in st_query[yr]:
        for state in st_query[yr][month]:
            if(state not in state_list):
                state_list[state] = []
            state_list[state] += st_query[yr][month][state]
            
eline =  open('preprocessing/distinct_govt_query', 'r').read().splitlines()
hline =  open('hindi_tranlations/nhindi.txt', 'r').read().splitlines()

e_h_trans = {}
for i in range(0,len(eline)):
    e_h_trans[eline[i]] = hline[i]

holding_dict = {'KARNATAKA':78322, 'PUNJAB':10526,
                'SIKKIM':749, 'HARYANA':16173, 
                'JAMMU AND KASHMIR':14494, 'HIMACHAL PRADESH':9608,
                'A AND N ISLANDS':118, 'TELANGANA':59094, 
                'TRIPURA':5785, 'NAGALAND':1784, 
                'MADHYA PRADESH':88724,'CHHATTISGARH':37465, 
                'DAMAN AND DIU':84, 'LAKSHADWEEP':103, 
                'RAJASTHAN':68884, 'BIHAR':161914, 
                'MAHARASHTRA':136990, 'DADRA AND NAGAR HAVELI':147, 
                'TAMILNADU':81182, 'MEGHALAYA':2096, 
                'GUJARAT':48856, 'CHANDIGARH':7, 
                'GOA':780, 'KERALA':68308, 
                'UTTAR PRADESH':233255, 'ODISHA':46675, 
                'PUDUCHERRY':332, 'ASSAM':27202, 
                'ANDHRA PRADESH':72657, 'DELHI':205, 
                'WEST BENGAL':71233, 'JHARKAND':27089, 
                'ARUNACHAL PRADESH':1093, 'MIZORAM':919, 
                'UTTARAKHAND':9127, 'MANIPUR':2523}


def get_scheme_count(key_wrd):
    ret_dict = {}
    ret2_dict = {}
    ocnt = 0
    for state in state_list:
        cnt = 0
        for query in state_list[state]:
            try:
                if(e_h_trans[query].find(key_wrd)!=-1):
                    cnt += 1
                    ocnt += 1
            except:
                continue
        ret_dict[state] = cnt
        ret2_dict[state] = cnt
    ans_list = [[ret_dict[state],state] for state in ret_dict]
    ans_list.sort()
    ans_list.reverse()
    return ans_list

def get_per_holding_scheme_count(key_wrd):
    ret_dict = {}
    ret2_dict = {}
    ocnt = 0
    for state in state_list:
        cnt = 0
        for query in state_list[state]:
            try:
                if(e_h_trans[query].find(key_wrd)!=-1):
                    cnt += 1
                    ocnt += 1
            except:
                continue
        ret_dict[state] = cnt/holding_dict[state]
        ret2_dict[state] = cnt
    ans_list = [[ret_dict[state],state] for state in ret_dict]
    ans_list.sort()
    ans_list.reverse()
    return ans_list

def get_queries(key_wrd):
    qset = {""}
    qlist = []
    cnt = 0
    for state in state_list:
        for query in state_list[state]:
            try:
                if((e_h_trans[query].find(key_wrd)!=-1) and (e_h_trans[query] not in qset)):
                    qset.add(e_h_trans[query])
                    qlist.append(e_h_trans[query])
                    cnt+=1
            except:
                continue
    qlist.sort()
    return qlist


### for the kcc part
scheme_count = get_scheme_count("kcc")
per_holding_count = get_per_holding_scheme_count("kcc")
qlist = get_queries("kcc")

qlist.sort()
with open('./kcc/kcc_queries_h.txt', 'w') as f:
    for item in qlist:
        f.write("%s\n" % item)
        
header1 = ["Frequency","State"]
with open('./kcc/output/state_counts.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header1)
    for elem in scheme_count:
        write.writerow(elem)

header2 = ["Frequency","State"]
with open('./kcc/output/per_holding_state_counts.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header1)
    for elem in per_holding_count:
        write.writerow(elem)

## for the samman nidhi part

scheme_count = get_scheme_count("सम्मान निधि")
per_holding_count = get_per_holding_scheme_count("सम्मान निधि")
qlist = get_queries("सम्मान निधि")

qlist.sort()
with open('./samman nidhi/samman_nidhi_h1.txt', 'w') as f:
    for item in qlist[0:int(len(qlist)*0.5)]:
        f.write("%s\n" % item)
with open('./samman nidhi/samman_nidhi_h2.txt', 'w') as f:
    for item in qlist[int(len(qlist)*0.5):]:
        f.write("%s\n" % item)

header1 = ["Frequency","State"]
with open('./samman nidhi/output/state_counts.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header1)
    for elem in scheme_count:
        write.writerow(elem)

header2 = ["Frequency","State"]
with open('./samman nidhi/output/per_holding_state_counts.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header1)
    for elem in per_holding_count:
        write.writerow(elem)


## for the mandhan part

scheme_count = get_scheme_count("मन धन")
per_holding_count = get_per_holding_scheme_count("मन धन")
qlist = get_queries("मन धन")

qlist.sort()
with open('./mandhan/mandhan_queries_h.txt', 'w') as f:
    for item in qlist:
        f.write("%s\n" % item)
        
header1 = ["Frequency","State"]
with open('./mandhan/output/state_counts.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header1)
    for elem in scheme_count:
        write.writerow(elem)

header2 = ["Frequency","State"]
with open('./mandhan/output/per_holding_state_counts.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header1)
    for elem in per_holding_count:
        write.writerow(elem)

## for the fasal bima part

scheme_count = get_scheme_count("फसल बीमा")
per_holding_count = get_per_holding_scheme_count("फसल बीमा")
qlist = get_queries("फसल बीमा")

qlist.sort()
with open('./fasal bima/fasal_bima_queries_h.txt', 'w') as f:
    for item in qlist:
        f.write("%s\n" % item)
        
header1 = ["Frequency","State"]
with open('./fasal bima/output/state_counts.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header1)
    for elem in scheme_count:
        write.writerow(elem)

header2 = ["Frequency","State"]
with open('./fasal bima/output/per_holding_state_counts.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header1)
    for elem in per_holding_count:
        write.writerow(elem)





