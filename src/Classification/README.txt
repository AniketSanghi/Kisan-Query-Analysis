Plugins-
Software: python3 jupyter notebook (.sh files run python3 jupyter notebooks)

Environments: conda 4.8.5, python 3.7.0

Dependencies-
Python Libraries: pandas 1.0.3, numpy 1.18.1, csv 1.0, tqdm, json 2.0.9, matplotlib 3.1.3, torch 1.6, sklearn 0.22.1, transformers 3.1.0, scipy 1.5.2, sentence_transformers 0.3.9, 

Location-
All scripts should be placed in 'src/Classification' folder.

Files used-
data.json file generated as a result of data scraping is used. data.json must be located inside 'src/data' folder.

Programs-

.sh files:

kcc_classification.sh 
top level script that runs all scripts required for classification

1.sh
runs 0_json_to_csv.py, 1_Data_Analysis_and_Data_Cleaning.py sequentially

2.sh
runs 2_Embeddings_generator.py, 3_Electra_Embeddings_generator.py, 4_SE_Embeddings_generator.py sequentially

3.sh
runs 7_Sector_Classification.py, 8_Sector_Classification_as_Regression.py, 9_Query_Type_Classification.py, 10_QueryType_Classification_as_Regression.py sequentially

4.sh
runs 11_Electra_Sector_Classification.py, 12_Electra_Sector_Classification_as_Regression.py, 13_Electra_Query_Type_Classification.py, 14_Electra_QueryType_Classification_as_Regression.py sequentially

5.sh
runs 15_SE_Sector_Classification.py, 16_SE_Sector_Classification_as_Regression.py, 17_SE_Query_Type_Classification.py, 18_SE_QueryType_Classification_as_Regression.py sequentially

Python (.py) files:

0_json_to_csv.py
Input: src/data/data.json
Output: Data.csv

1_Data_Analysis_and_Data_Cleaning.py
Input: Data.csv 
Output: final_sampled_data.csv, sector_sampled_data.csv

2_Embeddings_generator.py/ 3_Electra_Embeddings_generator.py/ 4_SE_Embeddings_generator.py
Input: final_sampled_data.csv, sector_sampled_data.csv
Output: querytype_dataset_sentence_embeddings.json, querytype_keys_sentence_embeddings.json, sector_dataset_sentence_embeddings.json, sector_keys_sentence_embeddings.json from BERT/ Electra/ Sentence Transformer respectively

7_Sector_Classification.py
Input: sector_sampled_data.csv, final_sector_dataset_sentence_embeddings.json
Output: Sector Classification using Decision Tree.jpg, Sector Classification using Random Forest.jpg, Sector Classification using linear SVM.jpg, Sector Classification using KNN classifier.jpg, Sector Classification using Naive Bayes classifier.jpg, Sector Classification using Logistic Regression.jpg 

8_Sector_Classification_as_Regression.py
Input: sector_sampled_data, final_sector_dataset_sentence_embeddings.json, sector_keys_sentence_embeddings.json
Output: Sector Regression using Classification as Regression technique.jpg

9_Query_Type_Classification.py
Input: final_sampled_data.csv, final_querytype_dataset_sentence_embeddings.json
Output: Query Type Classification using Decision Tree.jpg, Query Type Classification using Random Forest.jpg, Query Type Classification using linear SVM.jpg, Query Type Classification using KNN classifier.jpg, Query Type Classification using Naive Bayes classifier.jpg, Query Type Classification using Logistic Regression.jpg

10_QueryType_Classification_as_Regression.py
Input: final_sampled_data.csv, final_querytype_dataset_sentence_embeddings.json, querytype_keys_sentence_embeddings.json
Output: Query Type Regression using Classification as Regression technique.jpg

11 to 14.py - Same as 7 - 10.py for Electra Transformer

15 - 18.py - Same as 7 - 10.py for Sentence Transformer

How to use:
In order to run all programs sequentially, run the following 2 commands from the terminal-
chmod 700 *.sh
bash kcc_classification.sh

For Data Cleaning and Embedding Generation only-
bash 1.sh

For Multi-class Classification using BERT Embeddings-
bash 2.sh

For Multi-class Classification using Electra Embeddings-
bash 3.sh

For Multi-class Classification using Sentence Embeddings-
bash 4.sh