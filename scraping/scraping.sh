#! /bin/bash

python3 scraping.py 1 0 3653 &
python3 scraping.py 2 3653 7306 &
python3 scraping.py 3 7306 10959 &
python3 scraping.py 4 10959 14612 &

# wait for all subprocesses to complete
wait

# wait for downloading remaining files before combining them
sleep 20

bash combine.sh