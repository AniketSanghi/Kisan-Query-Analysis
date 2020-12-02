#!/bin/bash

cd src

python3 query_type_overall_processing.py

python3 overall_stats.py
python3 draw_overall_month_stats.py
python3 draw_overall_state_stats.py