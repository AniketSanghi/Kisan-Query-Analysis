import shlex
import re
import json

file1 = open('../hindi_tranlations/ohindi.txt', 'r')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
iLines = file1.read().splitlines()
Lines = []
for line in iLines:
    Lines.append(re.sub('[!*#?.\'()-;\[\]]+', ' ',line))

yojana_list = ['yajana', 'yajanao', 'yajona', 'yaojana', 'yjana', 'yoajan', 'yoajana', 'yoajna', 'yodagi', 'yogana', 'yogna', 'yogyna', 'yoijna', 'yojajan', 'yojama', 'yojana', 'yojanaa', 'yojanan', 'yojanao', 'yojane', 'yojanna', 'yojhana', 'yojn', 'yojna', 'yojnao', 'yojnaye', 'yojnayo', 'yojne', 'yojoana', 'yojona', 'yojuna', 'yojya', 'yona', 'yosana', 'yougana', 'youja', 'youjan', 'youjana', 'youjna', 'yoyona', 'yozana', 'yozna', 'yoznba', 'yozona', 'yzana']
nidhi_list = ['nddhi', 'ndhi', 'nedhi', 'nhidhi', 'niddhi', 'nidhe', 'nidhee', 'nidhhi', 'nidhi', 'nidhia', 'nidhib', 'nidhim', 'nidhin', 'nidhio', 'nidhis', 'nidhu', 'nidi', 'nidihi']
samman_list = ['ssaman', 'samn', 'samna', 'samnman', 'sanma', 'sanman', 'sanmman', 'sammma', 'sammman', 'sammn', 'sammna', 'samma', 'sammaaan', 'sammaan', 'sammam', 'samman', 'sammana', 'samaan', 'samad', 'saman', 'samana', 'smaan', 'smam', 'sman', 'smanman', 'snaman', 'smman', 'somman', 'summan']
samman_nidhi_list = ['समन नदि', 'समन नधि', 'सम्मान निधि', 'समन नहीं', 'समन नादि', 'समन निति', 'समन निथि', 'समन निथी', 'समन निदि', 'समन निधि', 'समन निधी', 'समन निमन', 'समन नीति', 'समन नीदे', 'समधन नधि', 'समधन निधि', 'समधी निधि', 'समाँ निधि', 'समां निधि', 'समाज निकंदी', 'समाज निदि', 'समाधि निधि', 'समान निधि', 'समस्या निधि', 'समाधान निधि', 'समि निधि', 'समिण निधि', 'समिति निधि', 'समिति निधी', 'समिध निधि', 'समिधन निधि', 'समिधा निधि', 'समिधि निधि', 'समृद्धि निधि', 'सम्पत्ति निधि', 'सम्मति निधि', 'सम्मन निदि', 'सम्मन निधि', 'सम्मन बिधि', 'सम्मनं निधि', 'सम्मान निधि', 'सम्मान निधिb', 'सम्मान निधिhi', 'सम्मान निधिn', 'सम्मान निधिs', 'सम्मान निधिy', 'साधना निधि', 'सानिध्य निधि', 'सामन निधि', 'सामर्थ्य निधि', 'सेम्मन निधि', 'समाज निधि', 'समन निधि', 'किसान निधि', 'संधि निधि', 'pmksn', 'सममान निधि', 'सम्\\u200dमान निधि', 'समिति निधि', 'सम्मन निधि', 'किसान समनिधि', 'समधी निधि', 'समधन निधि', 'संपर्क निधि', 'समाधि निधि', 'निधि निधि', 'सममन निधि', 'किसान सम्\\u200dमानिधि', 'समिधि निधि', 'शाम समनिधि', 'स्मान निधि', 'समाज नेदी', 'किशन निधि', 'संधी निधि', 'सम निधि', 'किसमन निधि', 'समनिधि निधि','निधि निधि', 'समनि निधि', 'सम्मानaan निधि', 'दोपहर निधि', 'सनमान निधि', 'शमन निधि', 'शामन निधि']
pm_list = ['पीएम', 'शाम', 'दोपहर']
pmfb_list = ['Fosal bima', 'bhasal bima', 'fasal bima', 'fasal vima', 'fasal बीमा', 'fasal भीम', 'fashal bima', 'fasl beema', 'fasal beema', 'fasl bheema', 'fasl bima', 'fhasal bima', 'fosol bima', 'fsal beema', 'fsal bima', 'fasal beema', 'fasal bheema', 'fasal bhema', 'fasal bhima', 'fasal chhati', 'fasal fima', 'fasalbhima', 'phalhal bima', 'phas bima', 'phasal bheema', 'phasal bima', 'phasala bhima', 'phasala bima', 'phsal bheema', 'phsal बिमा', 'pik vima', 'pasal bheema', 'pasal bhima', 'kisan bima', 'फशल बीमा', 'फसली बीमा', 'फशल भीम', 'फशल विमा', 'फशाल बिमा', 'फशाल बीमा', 'फसमल बीमा', 'फसल बिमा', 'फसल बीज', 'फसल बीमा', 'फसला बीमा', 'फसला भाव', 'फसला भीम', 'फसाल बिमा', 'फसाल बीमा', 'फसाला बीमा', 'फस्यल बीमा', 'फस्लिमा बीमा', 'फस्ले बिमा', 'फ़सल बीमा', 'फ़सला बीमा', 'फ़सली बिमा', 'फ़साल बिमा', 'फ़साल बीमा', 'फ़साल सीमा', 'फ़ासल बीमा', 'फ़ासला बीमा', 'फ़िशल बीमा', 'फ़ेसल बिमा', 'फ़ेसल बीमा', 'फासल बिमा', 'फासल बीमा', 'फासल भीम', 'फासला बिमा', 'फासला बीमा', 'फासला भीम', 'फासला वेमा', 'फासले भीम', 'फासिमा बीमा', 'फासिल बीमा', 'फिमल बीमा', 'फिमेल बीमा', 'फिशल बीमा', 'फिस्टल बीमा', 'फेमल बीमा', 'फेसल बीमा', 'फेसल बीमे', 'फेसल भीम', 'फेसला बीमा', 'फेसाल बीमा', 'फेसाल विमा', 'फेसिमा बीमा', 'फैसल बिमा', 'फैसल बीम', 'फैसल बीमा', 'फैसल बोमा', 'फैसल भामा', 'फैसल भीम', 'फैसल विमा', 'फैसाल बीमा', 'फोसोल बिमा', 'फसल बीमा', 'फसल बीमाा', 'फालसा बीमा', 'फालसा भीम', 'फाल्स बीमा', 'फासक बीमा', 'फासल विमा', 'फैस बीमा', 'फ़ासिमा बीमा', 'pmफसल बीमा', 'pm बीमा', 'fsal बीमा', 'pm fby', 'pmfb']
kcc_list = ['kcc', 'credit card', 'क्रेडिट कार्ड', 'क्रेडिट कार्ड', 'क्रेडिटकार्ड', 'किसान क्रेडिट', 'किसान क्रेडिटकार्ड']
mandhan_list = ['मन्धन', 'आदमी दान', 'आदमी धन', 'mandhan', 'pmmkisan', 'pmkmisan mandhan', 'pm मंडन', 'pm मंथन', 'pm मंधा', 'pm मंधान', 'pm मंधाना', 'pm मण्डन', 'pm मन्थन', 'pm मन्धन', 'shramayogi mandhan', 'yogi mandhan', 'किसान mandan', 'किसान mandhan', 'pm maandhan', 'pm manadhan', 'man dhaan', 'man dhan', 'mandhan penshan', 'mann dhan', 'mann dhann', 'mannn dhan', 'maan dan', 'maan dhaan', 'maan dhan', 'maan dhana', 'maan dhen', 'maandhan','किसान धन','मान धन','मानव धन','मनधन','मानधन','माँधन','महाधन','माँ धन','मानवधन']


#replacing the word in the list
def replace_wrds(str_list,substr):
    ind = 0
    for i in range(0,len(Lines)):
        for wrd in str_list:
            if(Lines[i].find(wrd) != -1):
                Lines[i] = Lines[i].replace(wrd, substr)


replace_wrds(yojana_list,"योजना")
replace_wrds(nidhi_list,"निधि")
replace_wrds(samman_list,"सम्मान")
replace_wrds(["सम्मानn"],"सम्मान")
replace_wrds(samman_nidhi_list,"सम्मान निधि")
replace_wrds(pm_list,"pm")
replace_wrds(['pm किसान योजना'],"सम्मान निधि")
replace_wrds(pmfb_list,"फसल बीमा")
replace_wrds(kcc_list,"kcc")
replace_wrds(mandhan_list,"मन धन")

with open('../hindi_tranlations/nhindi.txt', 'w') as f:
    for item in Lines:
        f.write("%s\n" % item)