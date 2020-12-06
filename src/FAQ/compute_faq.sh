#!/bin/bash

[ ! -d "library" ] && mkdir library
[ ! -d "images" ] && mkdir images

cd src

python3 compute_faq.py "$@"

cd ..