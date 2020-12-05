#! /bin/bash

dirs=(
    general_analysis
    per_crop_disease_analysis
    statewise_analysis
    monthwise_analysis
)

for dir in ${dirs[@]}
do
    cd $dir
    bash run.sh
    cd ..
done