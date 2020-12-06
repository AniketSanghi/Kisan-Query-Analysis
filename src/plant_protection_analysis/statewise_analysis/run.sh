#! /bin/bash

mkdir -p data plots

cd src
python3 freq_crop_per_state.py "Paddy (Dhan)" paddy_data
python3 freq_crop_per_state.py "Cotton (Kapas)" cotton_data
python3 freq_crop_per_state.py "Wheat" wheat_data

python3 make_plot.py paddy_data
python3 make_plot.py cotton_data
python3 make_plot.py wheat_data
cd ..