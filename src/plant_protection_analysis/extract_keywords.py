# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re

# def get_top_features(corpus, top_n):
#     vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,3))
#     X = vectorizer.fit_transform(corpus)
#     indices = np.argsort(vectorizer.idf_)[::-1]
#     features = vectorizer.get_feature_names()
#     top_features = [features[i] for i in indices[:top_n]]
#     return top_features

def init():
    extra_stop_words_list = ['^ask.*', '^control.*', '^tell.*', '^farmer.*', '^want.*', '^need.*', '^know.*', '^information.*', '^regard.*', '^crop.*', '^measure.*']
    extra_stop_words.update(extra_stop_words_list)

    mappings = {}
  
def filter_sentence(sentence):
    sentence = re.sub(r'[^a-zA-Z ]+', ' ', sentence)
    word_tokens = word_tokenize(sentence)  
    
    # sentence = [ps.stem(w) for w in word_tokens]
    sentence = word_tokens
    sentence = [w for w in sentence if not w in stop_words]
    sentence = [w for w in sentence if all(not re.search(x, w) != None for x in extra_stop_words)]

    sentence = [mappings.get(w, w) for w in sentence]
    if 'contact' in sentence:
        sentence = []
    sentence = ' '.join(sentence)

    return sentence    

stop_words = set(stopwords.words('english'))
extra_stop_words = set()
mappings = {}
ps = PorterStemmer()
init()
if __name__ == '__main__':
    # corpus = [
    #     'This is the first document.',
    #     'This document is the second document.',
    #     'And this is the third one.',
    #     'Is this the first document?',
    # ]
    # top_n = 3
    # top_features = get_top_features(corpus, top_n)
    # print(top_features)

    example_sent = """This is a sample sentence, 
                  showing off the stop words filtration asking."""
    output = filter_sentence(example_sent)
    print(output) 