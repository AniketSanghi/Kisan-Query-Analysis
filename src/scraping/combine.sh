#! /bin/bash

mkdir -p ../data/dataset
count=`ls ../data/dataset | wc -l`

for file in ./data/data_{1,2,3,4}/*
do
    cp $file "../data/dataset/$count.csv"
    count=$((count+1))
done
