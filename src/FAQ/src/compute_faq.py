# pip3 install -U sentence-transformers

import csv
import json
import numpy as np
from sentence_transformers import SentenceTransformer, util
import sys

def compute_count(cluster, query_freq, corpus):
    total_count = 0
    for idx in cluster:
        sentence = corpus[idx]
        freq = query_freq[sentence]
        total_count += freq
    return total_count


# Code Taken from https://github.com/UKPLab/sentence-transformers/blob/master/examples/applications/clustering/fast_clustering.py
def clustering_based_on_cosine_similarity(embeddings, threshold=0.75, min_community_size=10, init_max_size=1000):

    # Compute cosine similarity scores
    cos_scores = util.pytorch_cos_sim(embeddings, embeddings)

    # Minimum size for a community
    top_k_values, _ = cos_scores.topk(k=min_community_size, largest=True)

    # Filter for rows >= min_threshold
    extracted_communities = []
    for i in range(len(top_k_values)):
        if top_k_values[i][-1] >= threshold:
            new_cluster = []

            # Only check top k most similar entries
            top_val_large, top_idx_large = cos_scores[i].topk(k=init_max_size, largest=True)
            top_idx_large = top_idx_large.tolist()
            top_val_large = top_val_large.tolist()

            if top_val_large[-1] < threshold:
                for idx, val in zip(top_idx_large, top_val_large):
                    if val < threshold:
                        break

                    new_cluster.append(idx)
            else:
                # Iterate over all entries (slow)
                for idx, val in enumerate(cos_scores[i].tolist()):
                    if val >= threshold:
                        new_cluster.append(idx)

            extracted_communities.append(new_cluster)

    

    # Step 2) Remove overlapping communities
    unique_communities = []
    extracted_ids = set()

    # Largest cluster first
    for community in sorted(extracted_communities, key=lambda x: len(x), reverse=True):
        add_cluster = True
        for idx in community:
            if idx in extracted_ids:
                add_cluster = False
                break

        if add_cluster:
            unique_communities.append(community)
            for idx in community:
                extracted_ids.add(idx)

    return unique_communities


args = {
    "year": "",
    "month": "",
    "state": "",
    "district": "",
    "crop": "",
}

# interpret arguments
for i in range(1, len(sys.argv)):
    myargs = sys.argv[i][2:].split('=')
    args[myargs[0]] = myargs[1]

print("Computing FAQ for - \n", args,"\n")

# Load Multilingual model
print("Loading model, wait...")
model = SentenceTransformer('xlm-r-bert-base-nli-stsb-mean-tokens')
print("Model loaded successfully\n")


print("Loading dataset, wait...")
with open('../../data/data.json') as file:
    data = json.load(file)

def preprocess(data):
    data = data.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|\"`~-=_+"})
    data = ' '.join(data.lstrip().rstrip().split())
    return data

total_query_count = 0
queries = {}
for year, months in data.items():
    for month, states in months.items():
        for state, districts in states.items():
            for district, data_list in districts.items():
                for elem in data_list:
                    sector = elem[0]
                    category = elem[1]
                    crop = elem[2]
                    query_type = elem[3]
                    query = elem[4]

                    curr_data = {
                        "year": year,
                        "month": month,
                        "state": state,
                        "district": district,
                        "crop": crop,
                    }

                    to_take = True
                    for key in curr_data.keys():
                        if args[key] != "":
                            if args[key].lower() not in curr_data[key].lower():
                                to_take = False
                                break

                    if not to_take:
                        continue

                    query = preprocess(query)
                    total_query_count += 1

                    if query in queries.keys():
                        queries[query] += 1
                    else:
                        queries[query] = 1


corpus_sentences = []
for query in sorted(queries.keys()):
    corpus_sentences.append(query)

print("Dataset loaded successfully!")
print("Total queries = ", total_query_count, "\n")


print("Encode the corpus. This might take a while...")
corpus_embeddings = model.encode(corpus_sentences, show_progress_bar=True, convert_to_numpy=True)

#Compute cosine similarity between all pairs
print("Start clustering")

#Two parameter to tune:
#min_cluster_size: Only consider cluster that have at least 25 elements (30 similar sentences)
#threshold: Consider sentence pairs with a cosine-similarity larger than threshold as similar
clusters = clustering_based_on_cosine_similarity(corpus_embeddings, min_community_size=1, threshold=0.9, init_max_size=min(1000, len(queries.keys())))

# Sort clusters based on actual cluster size
clusters.sort(key=lambda x: compute_count(x, queries, corpus_sentences), reverse=True)


# File Suffix calculator
order = ["year", "month", "state", "district", "crop"]
suffix = []
for key in order:
    if args[key] != "":
        suffix.append(args[key].upper())

final_suffix = '-'.join(suffix)

print("Computing FAQs...")
top10 = 10
with open("../library/FAQ-" + final_suffix + ".txt", 'w', newline='') as file:
    writer = csv.writer(file)
    for cluster in clusters:
        count = compute_count(cluster, queries, corpus_sentences)
        writer.writerow([corpus_sentences[cluster[0]]])
        top10 -= 1
        if top10 == 0:
            break

with open("../library/Clusters-" + final_suffix + ".txt", 'w') as file:
    for i, cluster in enumerate(clusters):
        file.write("\nCluster {}, #Represents {} Elements \n".format(i+1, compute_count(cluster, queries, corpus_sentences)))
        for sentence_id in cluster:
            file.write("\t" + corpus_sentences[sentence_id] + "\n")

print("FAQ computed! Can be found at src/FAQ/library/FAQ-" + final_suffix + ".txt","\n")

