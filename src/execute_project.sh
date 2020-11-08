#!/bin/bash

# This function will process any flags, if given
preprocess_args () {
	# Risky flag
	# Fetching can take upto 24hours or more
	# Preprocessing takes 10-20mins
	# Uncomment both bash execute calls to make this runnable
	if [ $1 = "--fetch" ]; then
		echo "---> Scraping Data "
		cd scraping
		bash scraping.sh
		cd ..
	fi
	if [ $1 = "--preprocess" ]; then
		echo "---> Preprocessing Data "
		cd preprocessing
		bash preprocess.sh
		cd ..
	fi
}

for var in "$@"
do
    preprocess_args $var
done