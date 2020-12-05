--------------------------------------------------------------------------------------------------------------
						##### HIGHLIGHTS ######
--------------------------------------------------------------------------------------------------------------

- The code may take arbitrary amount of time (atmax 48hrs) depending on parameters (or total queries)


--------------------------------------------------------------------------------------------------------------
						##### DEPENDENCIES #####
--------------------------------------------------------------------------------------------------------------

- bash
- python3.7.1 (python 3.6 and above should be fine)
	libraries
		- json
		- csv
            - numpy
            - sys
            - sentence_transformers

--------------------------------------------------------------------------------------------------------------
						##### HOW TO RUN #####
--------------------------------------------------------------------------------------------------------------

- To compute the FAQs for the overall data
========> bash compute_faq.sh

- You can find FAQ of a subset of data by giving space separated parameters to the executable
========> bash compute_faq.sh --<param_name1>=<param_value1> --<param_name2>=<param_value2>

Allows params
| --year      - in range [2018, 2020]
| --month     - in range [1 - 12]
| --state     - for possible values you can check src/General\ Analysis/library/overall_state_frequency.csv
| --district  - for possible values you can check src/General\ Analysis/library/overall_district_frequency.csv
| --crop      - for possible values you can check src/General\ Analysis/library/overall_crop_frequency.csv

Examples
--------
========> bash compute_faq.sh --year=2019 --month=8 --state="uttar pradesh" --crop="paddy"
========> bash compute_faq.sh --district=raipur
========> bash compute.faq.sh --crop=wheat --year=2018

--------------------------------------------------------------------------------------------------------------
                                    ##### HOW TO EVALUATE #####
--------------------------------------------------------------------------------------------------------------
For every run 2 output files will be generated in src/FAQ/library/

They are prefixed with
  - FAQ -> Contains the top 10 most frequently asked queries for the given sub-data
  - CLUSTERS -> This shows the clusters so formed, you can evaluate them to see how accurate it is
             -> Note that for each cluster, the <x> in line (Represents <x> Elements) in output file
             -> is the actual number of queries for that data. This value can be greater than cluster
             -> size as clustering is done only on unique queries. But actual count is used to generate
             -> final output files.