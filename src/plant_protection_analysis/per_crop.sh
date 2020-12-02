#! /bin/bash

python3 $1.py > "$1_rem.txt"
python3 "$1_freq.py" > "$1_freq.txt"