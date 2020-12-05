import json
import csv
import matplotlib.pyplot as plt
import numpy as np
import sys
with open('../data/data.json','r') as fh:
	result_dict=json.load(fh)
count=0
flist=[]
tempppp=0
paramlist=[]
cyclonelist=[]
earlylist=[]
latelist=[]
rainlist = []
for year in result_dict.keys():
	for month in result_dict[year].keys():
		for state in result_dict[year][month].keys():
			for city in result_dict[year][month][state].keys():
				for item in result_dict[year][month][state][city]:
					if "Weather" == item[3] :
						tempppp=tempppp+1
						if item[4].find("weather")!=-1 or item[4].find("werther")!=-1 or item[4].find("whaeather")!=-1 or item[4].find("mausam")!=-1 or item[4].find("wheather")!=-1 or item[4].find("temperature")!=-1 or item[4].find("rainfall")!=-1 or item[4].find("forecast")!=-1 or item[4].find("rain")!=-1 or item[4].find("monsoon")!=-1 or item[4].find("mausum")!=-1 or item[4].find("rain")!=-1 or item[4].find("weathr")!=-1 or item[4].find("weatehr")!=-1 or item[4].find("cyclone")!=-1 or item[4].find("whether")!=-1 or item[4].find("wethare")!=-1 or item[4].find("mansoon")!=-1 or item[4].find("raining")!=-1 or item[4].find("mosam")!=-1 or item[4].find("waether")!=-1 or item[4].find("weaather")!=-1 or item[4].find("weathe")!=-1 or item[4].find("w4ather")!=-1 or item[4].find("imd")!=-1 or item[4].find("weathewr")!=-1 :
						    if item[4].find("cyclone")!=-1 :
								cyclonelist.append(month+state)
						    if item[4].find("rain")!=-1 or item[4].find("rainfall")!=-1 or item[4].find("raining")!=-1 or item[4].find("monsoon")!=-1 or item[4].find("mansoon")!=-1:
								rainlist.append(month+state)

						    if year=="2018":
						    	earlylist
						    count=count+1
						    llist=[]
						    llist.append(month)
						    llist.append(state)
						    flist.append(llist)
						    paramlist.append(item[4])
						    if year=="2019":
						    	earlylist.append(llist)
						    if year=="2020":
						    	latelist.append(llist)	

statelist=[]
for year in result_dict.keys():
	for month in result_dict[year].keys():
		for state in result_dict[year][month].keys():
			if state not in statelist:
				statelist.append(state)
						
statecount={}
percentstatecount={}
monthcount={}
stateandmonthcount={}
julycount={}
octobercount={}
maycount={}
jancount={}
febcount={}
marcount={}
aprilcount={}
junecount={}
augustcount={}
sepcount={}
novcount={}
deccount={}
earlycount={}
latecount={}
latemonthcount={}
for element in earlylist:
	earlycount[element[1]]=0
for element in earlylist:
	earlycount[element[1]]=earlycount[element[1]]+1

for element in latelist:
	latecount[element[1]]=0
	latemonthcount[element[0]]=0
for element in latelist:
	latecount[element[1]]=latecount[element[1]]+1
	latemonthcount[element[0]]=latemonthcount[element[0]]+1



for element in flist:
	statecount[element[1]]=0

	monthcount[element[0]]=0
	stateandmonthcount[element[0]+'/'+element[1]]=0
	julycount[element[1]]=0
	octobercount[element[1]]=0
	maycount[element[1]]=0
	junecount[element[1]]=0
	jancount[element[1]]=0
	febcount[element[1]]=0
	marcount[element[1]]=0
	aprilcount[element[1]]=0
	augustcount[element[1]]=0
	sepcount[element[1]]=0
	novcount[element[1]]=0
	deccount[element[1]]=0

totalmaycount=0
totaloctobercount=0

for element in flist:
	statecount[element[1]]=statecount[element[1]]+1
	monthcount[element[0]]=monthcount[element[0]]+1
	stateandmonthcount[element[0]+'/'+element[1]]=stateandmonthcount[element[0]+'/'+element[1]]+1

for element in stateandmonthcount.keys():
	if '7' in element:
		julycount[element.split("/",1)[1]]=stateandmonthcount[element]
	if '10' in element:
		octobercount[element.split("/",1)[1]]=stateandmonthcount[element]
		totaloctobercount=totaloctobercount+1
	if '5' in element:
		maycount[element.split("/",1)[1]]=stateandmonthcount[element]
		totalmaycount=totalmaycount+1
	if '1' in element:
		jancount[element.split("/",1)[1]]=stateandmonthcount[element]
	if '2' in element:
		febcount[element.split("/",1)[1]]=stateandmonthcount[element]
	if '3' in element:
		marcount[element.split("/",1)[1]]=stateandmonthcount[element]
	if '4' in element:
		aprilcount[element.split("/",1)[1]]=stateandmonthcount[element]
	if '6' in element:
		junecount[element.split("/",1)[1]]=stateandmonthcount[element]
	if '8' in element:
		augustcount[element.split("/",1)[1]]=stateandmonthcount[element]
	if '9' in element:
		sepcount[element.split("/",1)[1]]=stateandmonthcount[element]
	if '11' in element:
		novcount[element.split("/",1)[1]]=stateandmonthcount[element]
	if '12' in element:
		deccount[element.split("/",1)[1]]=stateandmonthcount[element]	

		
keys=list(statecount.viewkeys())

jancorr=(np.corrcoef([statecount.get(x,0) for x in keys],[jancount.get(x,0) for x in keys])[0,1])
febcorr=(np.corrcoef([statecount.get(x,0) for x in keys],[febcount.get(x,0) for x in keys])[0,1])
marcorr=(np.corrcoef([statecount.get(x,0) for x in keys],[marcount.get(x,0) for x in keys])[0,1])
aprilcorr=(np.corrcoef([statecount.get(x,0) for x in keys],[aprilcount.get(x,0) for x in keys])[0,1])
maycorr=(np.corrcoef([statecount.get(x,0) for x in keys],[maycount.get(x,0) for x in keys])[0,1])
junecorr=(np.corrcoef([statecount.get(x,0) for x in keys],[junecount.get(x,0) for x in keys])[0,1])
julycorr=(np.corrcoef([statecount.get(x,0) for x in keys],[julycount.get(x,0) for x in keys])[0,1])
augcorr=(np.corrcoef([statecount.get(x,0) for x in keys],[augustcount.get(x,0) for x in keys])[0,1])
sepcorr=(np.corrcoef([statecount.get(x,0) for x in keys],[sepcount.get(x,0) for x in keys])[0,1])
octcorr=(np.corrcoef([statecount.get(x,0) for x in keys],[octobercount.get(x,0) for x in keys])[0,1])
novcorr=(np.corrcoef([statecount.get(x,0) for x in keys],[novcount.get(x,0) for x in keys])[0,1])
deccorr=(np.corrcoef([statecount.get(x,0) for x in keys],[deccount.get(x,0) for x in keys])[0,1])


percentmaycount={}
percentoctobercount={}
#for element in maycount.keys():
#	percentmaycount[element]=100.0*(maycount[element]/(1.0 * totalmaycount))
#for element in octobercount.keys():
#	percentoctobercount[element]=100.0*(octobercount[element]/(1.0 * totaloctobercount))

for element in statecount.keys():
	statecount[element]=statecount[element]
	percentstatecount[element]=100.0*(statecount[element]/(1.0 * count))

#for element in stateandmonthcount.keys():
#	print(element)

header=["State","Frequency"]


with open('percentstate.csv','w') as csv_file:
	writer=csv.writer(csv_file)
	writer.writerow(header)
	for key,value in percentstatecount.items():
		writer.writerow([key,value])

with open('state.csv','w') as csv_file:
	writer=csv.writer(csv_file)
	writer.writerow(header)
	for key,value in statecount.items():
		writer.writerow([key,value])

with open('julystate.csv','w') as csv_file:
	writer=csv.writer(csv_file)
	writer.writerow(header)
	for key,value in julycount.items():
		writer.writerow([key,value])

with open('octoberstate.csv','w') as csv_file:
	writer=csv.writer(csv_file)
	writer.writerow(header)
	for key,value in octobercount.items():
		writer.writerow([key,value])


with open('maystate.csv','w') as csv_file:
	writer=csv.writer(csv_file)
	writer.writerow(header)
	for key,value in maycount.items():
		writer.writerow([key,value])


monthresult_list=sorted([[m,c] for m,c in monthcount.items()],key = lambda x: int(x[0]))

m=[x[0] for x in monthresult_list]
c=[x[1] for x in monthresult_list]

plt.bar(range(len(monthcount)),c)
_=plt.xticks(range(len(monthcount)),m)


plt.savefig('monthcount.png')



max={}

for i in statelist:
	smax=0
	curr=0
	for j in range(0,13):
		if str(j)+'/'+i not in stateandmonthcount.keys():
			continue
		if smax < stateandmonthcount[str(j)+'/'+i]:
			smax=stateandmonthcount[str(j)+'/'+i]
			curr=j

	max[i]=curr	


