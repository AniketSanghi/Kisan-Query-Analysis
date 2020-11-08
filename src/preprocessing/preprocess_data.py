import csv
import datetime
import json
from os import listdir
import re
import sys

print("--- Stats of pre-processing stage ---", file=sys.stderr)

data_json = {}
metadata = set()

# Consider data from Oct,2018 to Sept,2020 only
start_date = datetime.datetime(2018, 10, 1)
end_date = datetime.datetime(2020, 10, 1)
def is_outside_range(date):
    return (date < start_date or date >= end_date)

# There were many duplicat datasets on the government website
# Removing these in the pre-processing stage
def is_duplicate_dataset(year, month, state, district):
    if (year, month, state, district) not in metadata:
        metadata.add((year, month, state, district))
        return False
    return True

# Duplicate consecutive entries were found in data
# Reason could be network issues when storing data in DB
# Removing these as well in the pre-processing stage
def is_duplicate_data(line, prev_line, time, prev_time):
    return (line == prev_line and (time - prev_time).total_seconds() < 6)

# Many outliers like "Call Disconnected", calls  from another region
# and many others were present. We found that one of the common substring
# for all those queries was "Call". Using it to remove outliers.
outlier_key = "call"
def is_outlier(query):
    return re.search(r"\b" + outlier_key + r"\b", query, re.IGNORECASE)

# Format text to improve readability and detection
def format_data(query):
    query = query.replace('\n', ' ').replace('\t', ' ')
    query = ' '.join(query.split())
    query = '?'.join(query.split('?'))
    query = '.'.join(query.split('.'))
    query = query.lstrip().rstrip()
    return query

def format_data_list(data_list):
    for i in range(0, len(data_list)):
        data_list[i] = format_data(data_list[i])
    data_list[-1] = data_list[-1].lower()
    return data_list

# Adds data element to the Data JSON
def add_to_data_json(year, month, state, district, data_point):
    if year in data_json.keys():
        if month in data_json[year].keys():
            if state in data_json[year][month].keys():
                if district in data_json[year][month][state].keys():
                    data_json[year][month][state][district].append(data_point)
                else:
                    data_json[year][month][state][district] = [data_point]
            else:
                data_json[year][month][state] = {district: [data_point]}
        else:
            data_json[year][month] = {state: {district: [data_point]}}
    else:
        data_json[year] = {month: {state: {district: [data_point]}}}

number_of_dataset_duplications = 0
number_of_data_duplications = 0
number_of_outliers = 0

for i in range(0, len(listdir("../data/dataset"))):
    with open("../data/dataset/" + str(i) + ".csv") as data:
        # try/except block added to deal with the issue of very large rows of rubbish data
        try:
            isDuplicationTested = False
            prev_line = {}
            prev_time = datetime.datetime(2020, 1, 1, 10, 10, 10)
            for line in csv.DictReader(data):
                created_on = datetime.datetime.strptime(line["CreatedOn"].split('.')[0], '%Y-%m-%dT%H:%M:%S')

                # Sampling only datasets between Oct'2018 to Sept'2020 (both included)
                if is_outside_range(created_on):
                    break

                (year, month) = (created_on.year, created_on.month)
                (state, district) = (line["StateName"], line["DistrictName"])
                (sector, category, crop) = (line["Sector"], line["Category"], line["Crop"])
                (query_type, query) = (line["QueryType"], line["QueryText"])
                line.pop("CreatedOn", None)

                # Remove all duplicate datasets
                if not isDuplicationTested:
                    isDuplicationTested = True
                    if is_duplicate_dataset(year, month, state, district):
                        number_of_dataset_duplications += 1
                        break
                
                # Remove all outliers
                if is_outlier(query):
                    number_of_outliers += 1
                    continue

                # Don't consider queries too large in size
                query = format_data(query)
                if len(query) > 150:
                    continue
                
                # Remove all duplicate data rows
                if len(prev_line) != 0:
                    if is_duplicate_data(line, prev_line, created_on, prev_time):
                        number_of_data_duplications += 1
                        prev_line = line
                        prev_time = created_on
                        continue
                prev_line = line
                prev_time = created_on

                # Add data to JSON
                data_point = format_data_list([sector, category, crop, query_type, query])
                add_to_data_json(year, month, state, district, data_point)
        except:
            print("File " + str(i) + ".csv had a very large row (outlier)", file=sys.stderr)

print("Number of duplicate datasets = " + str(number_of_dataset_duplications), file=sys.stderr)
print("Number of duplicate data = " + str(number_of_data_duplications), file=sys.stderr)
print("Number of outliers = " + str(number_of_outliers), file=sys.stderr)

with open('../data/data.json', 'w', encoding='utf8') as outfile:
    outfile.write(json.dumps(data_json, indent=0, ensure_ascii=False))
