import csv
import json

with open('./preprocessing/yr_st_gov_sch.json') as f:
    st_dict = json.load(f)
    
state_list = {}
for yr in st_dict:
    for month in st_dict[yr]:
        for state in st_dict[yr][month]:
            if(state not in state_list):
                state_list[state] = []
            state_list[state] += st_dict[yr][month][state]
            
state_counts = {}
for key in state_list:
    state_counts[key] = [0]*6


def scheme_queries(substr,qlist):
    ans_list = []
    for qi in qlist:
        try:
            if (e_h_trans[qi].find(substr)!=-1):
                ans_list.append(e_h_trans[qi])
        except:
            continue
    return ans_list

def wrd_present(dummy_list,qstr):
    for wrd in dummy_list:

        if(qstr.lower().find(wrd)!=-1):
            return True
    return False

## tagging part for the kcc
new_enlines =  open('./kcc/kcc_queries_en.txt', 'r').read().splitlines()
new_hlines =  open('./kcc/kcc_queries_h.txt', 'r').read().splitlines()

eline = open('./preprocessing/distinct_govt_query', 'r').read().splitlines()
hline = open('./hindi_tranlations/nhindi.txt', 'r').read().splitlines()

e_h_trans = {}
for i in range(0,len(eline)):
    e_h_trans[eline[i]] = hline[i]

h_e_trans = {}
for i in range(0,len(new_hlines)):
    h_e_trans[new_hlines[i]] = new_enlines[i].lower()
    

reg_list = ['register''eligibi','criteri','eligi','form','status','regist','digits','issue','time','complai','detai', 'limit','ban','descrip','date','docum','applic','appl','id']
finance_list = ['pin','payment','money','cost','claim','insur','pais','cashback','block','accou','fund','loan','bank','insurance','lon','intr','vyaj','inter']
contact_list = ['contact','help','line','number','sampark','message']
web_list = ['web','online',"www"]
general_info = ['where','make','inquir','ask','tell me','schem','about','jan','benef','query','quest','beneficia','jankar','explai','info','relat','feature']

# final counting
total_rc = total_fc = total_wc = total_gi = total_misc =  total_cc = 0
for state in state_list:
    qlist = scheme_queries("kcc",state_list[state])
    rc = fc = cc = wc = gi = misc = 0
    for q in qlist:
        q = h_e_trans[q]
        check = True
        if (wrd_present(web_list,q)):
            wc += 1
            check = False
        if (wrd_present(reg_list,q)):
            rc += 1
            check = False
        if (wrd_present(finance_list,q)):
            fc += 1
            check = False
        if (wrd_present(contact_list,q)):
            cc += 1
            check = False
        if (check and wrd_present(general_info,q) ):
            gi += 1
            check = False
        if (check and wrd_present(['janari'],q) ):
            gi += 1
            check = False
        if (check):
            misc += 1
    total_rc += rc ; total_fc += fc; total_cc += cc
    total_wc += wc ; total_gi += gi; total_misc += misc
    state_counts[state] = [rc,fc,cc,wc,gi,misc]

state_csv = []
for state in state_counts:
    state_csv.append([state]+state_counts[state])
state_csv.sort()
header = ["state","registration","financial","contacting","website","general info","not tagged"]
trow = ["total",total_rc,total_fc,total_cc,total_wc,total_gi,total_misc]

with open('./kcc/output/state_wise_problems.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header)
    for elem in state_csv:
        write.writerow(elem)
    write.writerow(trow)

## tagging part for the mandhan

for key in state_list:
    state_counts[key] = [0]*6

new_enlines =  open('./mandhan/mandhan_queries_en.txt', 'r').read().splitlines()
new_hlines =  open('./mandhan/mandhan_queries_h.txt', 'r').read().splitlines()

eline = open('./preprocessing/distinct_govt_query', 'r').read().splitlines()
hline = open('./hindi_tranlations/nhindi.txt', 'r').read().splitlines()

e_h_trans = {}
for i in range(0,len(eline)):
    e_h_trans[eline[i]] = hline[i]

h_e_trans = {}
for i in range(0,len(new_hlines)):
    h_e_trans[new_hlines[i]] = new_enlines[i].lower()
    

reg_list = ['apply','panji','age','eligibility','regis','applicat','ocuments','time','information','omar']+["apply",'date','plan','application','form','registration','report','filling']
finance_list =  ['account','pais','income','pension','money', 'wealth','installment','insurance','rupay','fund'] + ['loan','subsid','primium','financial','kcc','cliam',"compensation","premium",'fund','pay','paisa','card','credit','claim','money','bank','status','company']
contact_list = ['phone','help','toll','free','contact',"sampark","message"]
web_list = ['web','online',"www"]
general_info = ['description','what','know','jaanka','jank','detai', 'bare','inf'] + ['jankari','policy','about','tell','labh','know','about'"general","deadline","ask","list","regarding",'inform','details','related','questions','explain','information','janri']

total_rc = total_fc = total_wc = total_gi = total_misc =  total_cc = 0
for state in state_list:
    qlist = scheme_queries("मन धन",state_list[state])
    rc = fc = cc = wc = gi = misc = cropc = 0
    for q in qlist:
        q = h_e_trans[q]
        check = True
        if (wrd_present(web_list,q)):
            wc += 1
            check = False
        if (wrd_present(reg_list,q)):
            rc += 1
            check = False
        if (wrd_present(finance_list,q)):
            fc += 1
            check = False
        if (wrd_present(contact_list,q)):
            cc += 1
            check = False
        if (check and wrd_present(general_info,q) ):
            gi += 1
            check = False
        if (check and wrd_present(['janari'],q) ):
            gi += 1
            check = False
        if (check):
            misc += 1
    total_rc += rc ; total_fc += fc; total_cc += cc
    total_wc += wc ; total_gi += gi; total_misc += misc
    state_counts[state] = [rc,fc,cc,wc,gi,misc]

state_csv = []
for state in state_counts:
    state_csv.append([state]+state_counts[state])
state_csv.sort()
header = ["state","registration","financial","contacting","website","general info","not tagged"]
trow = ["total",total_rc,total_fc,total_cc,total_wc,total_gi,total_misc]

with open('./mandhan/output/state_wise_problems.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header)
    for elem in state_csv:
        write.writerow(elem)
    write.writerow(trow)

## tagging part for fasal bima

for key in state_list:
    state_counts[key] = [0]*6

new_enlines =  open('./fasal bima/fasal_bima_queries_en.txt', 'r').read().splitlines()

new_hlines =  open('./fasal bima/fasal_bima_queries_h.txt', 'r').read().splitlines()

eline = open('./preprocessing/distinct_govt_query', 'r').read().splitlines()
hline = open('./hindi_tranlations/nhindi.txt', 'r').read().splitlines()

e_h_trans = {}
for i in range(0,len(eline)):
    e_h_trans[eline[i]] = hline[i]

h_e_trans = {}
for i in range(0,len(new_hlines)):
    h_e_trans[new_hlines[i]] = new_enlines[i].lower()
    

reg_list = ["apply","sampark","message",'date','plan','application','form','registration','report','filling']
finance_list = ['loan','subsid','primium','financial','kcc','cliam',"compensation","premium",'fund','pay','paisa','card','credit','claim','money','bank','status','company']
contact_list = ['phone','helpline','toll','free','contact']
web_list = ['web','online',"www"]
crop_list = ['kharif',"krif","rabi","paddy","wheat"]
general_info = ['jankari','policy','about','tell me','labh','crop insurance scheme','know','about'"general","deadline","ask","list","regarding",'inform','details','related','questions','explain','information','janri','crop insurance y']

total_rc = total_fc = total_wc = total_gi = total_misc = total_cropc = total_cc = 0
for state in state_list:
    qlist = scheme_queries("फसल बीमा",state_list[state])
    rc = fc = cc = wc = gi = misc = 0
    for q in qlist:
        q = h_e_trans[q]
        check = True
        if (wrd_present(web_list,q)):
            wc += 1
            check = False
        if (wrd_present(reg_list,q)):
            rc += 1
            check = False
        if (wrd_present(finance_list,q)):
            fc += 1
            check = False
        if (wrd_present(contact_list,q)):
            cc += 1
            check = False
        if (check and wrd_present(general_info,q) ):
            gi += 1
            check = False
        if (check and wrd_present(['janari'],q) ):
            gi += 1
            check = False
        if (check and (wrd_present(crop_list,q))):
	        cropc += 1
	        check = False
        if (check):
            misc += 1
    total_rc += rc ; total_fc += fc; total_cc += cc; total_cropc += cropc
    total_wc += wc ; total_gi += gi; total_misc += misc
    state_counts[state] = [rc,fc,cc,wc,gi,cropc,misc]

state_csv = []
for state in state_counts:
    state_csv.append([state]+state_counts[state])
state_csv.sort()
header = ["state","registration","financial","contacting","website","general info","crop related","not tagged"]
trow = ["total",total_rc,total_fc,total_cc,total_wc,total_gi,total_cropc,total_misc]

with open('./fasal bima/output/state_wise_problems.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header)
    for elem in state_csv:
        write.writerow(elem)
    write.writerow(trow)

## samman nidhi part

new_enlines =  open('./samman nidhi/samman_nidhi_en1.txt', 'r').read().splitlines()
new_enlines += open('./samman nidhi/samman_nidhi_en2.txt', 'r').read().splitlines()

new_hlines =  open('./samman nidhi/samman_nidhi_h1.txt', 'r').read().splitlines()
new_hlines +=  open('./samman nidhi/samman_nidhi_h2.txt', 'r').read().splitlines()

eline = open('./preprocessing/distinct_govt_query', 'r').read().splitlines()
hline = open('./hindi_tranlations/nhindi.txt', 'r').read().splitlines()

e_h_trans = {}
for i in range(0,len(eline)):
    e_h_trans[eline[i]] = hline[i]

h_e_trans = {}
for i in range(0,len(new_hlines)):
    h_e_trans[new_hlines[i]] = new_enlines[i].lower()

reg_list = ["notice",'id ',"beneficiary","rajitration","rejected","aadhar",'address','register','eligibility','apply','details','panjikaran','form','document','aadhaar','application','registration']
finance_list = ["reimbursement","bank","pisa","ifsc","code","khatoni",'rupees','paise','balance','benefit','khata','financial assistance','fund','credit','paisa','transfer','payment','account','status','installment','money']
contact_list = ['number','phone','toll','help line','helpline','contact']
web_list = ["http","www",'website','onlin','link','site',"nic"]
general_info = ["related","problem","question",'asked','pm kisan samman nidhi','know','regarding','abou','tell me','janaki','asked about','questions','explain','information','jankari', 'query','information about']

total_rc = total_fc = total_wc = total_gi = total_misc = total_cc =  0
for state in state_list:
    qlist = scheme_queries('सम्मान निधि',state_list[state])
    rc = fc = cc = wc = gi = misc = 0
    for q in qlist:
        q = h_e_trans[q]
        check = True
        if (wrd_present(web_list,q)):
            wc += 1
            check = False
        if (wrd_present(reg_list,q)):
            rc += 1
            check = False
        if (wrd_present(finance_list,q)):
            fc += 1
            check = False
        if (wrd_present(contact_list,q)):
            cc += 1
            check = False
        if (check and (wrd_present(general_info,q) or q=='pkimsan samman nidhi yojana' or q=='prime minister kisan samman nidhi yojana') ):
            gi += 1
            check = False
        if (check and wrd_present(['janari'],q) ):
            gi += 1
            check = False
        if (check):
            misc += 1
    total_rc += rc ; total_fc += fc; total_cc += cc
    total_wc += wc ; total_gi += gi; total_misc += misc
    state_counts[state] = [rc,fc,cc,wc,gi,misc]

state_csv = []
for state in state_counts:
    state_csv.append([state]+state_counts[state])
state_csv.sort()
header = ["state","registration","financial","contacting","website","general info","not tagged"]
trow = ["total",total_rc,total_fc,total_cc,total_wc,total_gi,total_misc]

with open('./samman nidhi/output/state_wise_problems.csv', 'w') as f: 
    write = csv.writer(f)  
    write.writerow(header)
    for elem in state_csv:
        write.writerow(elem)
    write.writerow(trow)