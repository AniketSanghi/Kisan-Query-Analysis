## Programming Language Required
- python 3.6.9

## Packages Required
* matplotlib
* nltk
* psutil
* kaleido

## Directory Structure
There are 4 sub-categories under Plant Protection and each analysis is in separate directory.
1. general_analysis
2. per_crop_disease_analysis
3. statewise_analysis
4. monthwise_analysis

Each of the above 4 directories has the below directory structure
```
.
├── clean.sh
├── data
│   └── *.csv
├── plots
│   └── *.png
├── run.sh
└── src
    └── *.py
```

1. clean.sh removes all the output files present in the directories data and plot
2. data contains all the generated csv files
3. plots contains all the graphs obtained from csv files
4. run.sh runs all the python files to generate csv and plots
5. src contains all the code for generating csv and plots 

There is directory `plots` in the current directory which contains the code for plotting data on India map.

## How to execute
```
chmod 700 *.sh
bash run.sh
```
This bash script calls all the top levels scripts in the above 4 directories which in turn generate csv files and plots in their own respective directories.

## How to remove the output files
```
chmod 700 *.sh
bash clean.sh
```
This bash script calls all the top level cleanup scripts to remove every output file like .csv and .png from each of these 4 directories.

## Description:
- Avg. time taken to run: 5 mins 21 seconds on a 2.30GHz, 64-bit, 8GB RAM machine.
- general_analysis:
  - top_crop_count.py: finds queries of major crops related to plant protection
  - freq_per_state.py: finds states in which majority of plant protection queries were asked
  - make_plot.py: imports a package to make India map which is located in src/library from the root directory of the project. 
  - make_piechart.py: makes a piechart.
- per_crop_disease_analysis:
  - extract_keywords.py: given a sentence as input, returns filtered sentence 
  - relevant_words.py: narrows down the data to fetch only relevant queries
  - cotton.py: finds major categories in cotton queries 
  - paddy.py: finds major categories in paddy queries 
  - wheat.py: finds major categories in wheat queries 
  - make_piechart.py: makes a piechart.
- statewise_analysis:
  - freq_crop_per_state.py: finds major states where queries regarding a given crop are asked.
  - make_piechart.py: makes a piechart.
- monthwise_analysis:
  - freq_crop_per_month.py: finds major months when queries regarding a given crop are asked.
  - make_piechart.py: makes a piechart.
