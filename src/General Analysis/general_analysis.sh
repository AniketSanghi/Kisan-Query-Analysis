#!/bin/bash

cd src

echo "Computing frequency for various query types..."
echo ""
python3 compute_query_type_stats.py

echo "Generating CSVs storing stats..."
echo ""
python3 compute_overall_stats.py

echo "Drawing charts displaying stats
"
python3 draw_query_type_piechart.py
python3 draw_overall_month_stats.py
python3 draw_overall_state_stats.py
python3 draw_crop_piechart.py