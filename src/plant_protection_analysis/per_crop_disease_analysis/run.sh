#! /bin/bash

cd src
python3 relevant_words.py
python3 paddy.py
python3 cotton.py
python3 wheat.py

python3 make_piechart.py paddy_data
python3 make_piechart.py cotton_data
python3 make_piechart.py wheat_data
cd ..