file = open('distinct_govt_query','r')
Lines = file.read().splitlines()

for i in range(0,24):
	n_lines = Lines[int(i*0.5*10000):int((1+i)*0.5*10000)]
	with open('./batches/temp_translation'+str(i)+'.txt', 'w') as f:
	    for item in n_lines:
	        f.write("%s\n" % item)

n_lines = Lines[int(12.0*10000):-1]
with open('./batches/temp_translation24.txt', 'w') as f:
    for item in n_lines:
        f.write("%s\n" % item)