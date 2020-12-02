import csv
import sys

with open("../data/"+sys.argv[1]+".csv", 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 
      
    fields = next(csvreader) 
  
    cnt = 0
    for row in csvreader: 
        cnt += int(row[1])
    print(cnt)