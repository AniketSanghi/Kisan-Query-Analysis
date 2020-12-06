#! /bin/bash

mkdir -p data plots

cd src
python3 freq_crop_per_month.py "Paddy (Dhan)" paddy_data
python3 freq_crop_per_month.py "Cotton (Kapas)" cotton_data
python3 freq_crop_per_month.py "Wheat" wheat_data

python3 make_plot.py paddy_data Paddy
python3 make_plot.py cotton_data Cotton
python3 make_plot.py wheat_data Wheat
cd ..