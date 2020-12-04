from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

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
# ps = PorterStemmer()
init()


if __name__ == '__main__':

    example_sent = """This is a sample sentence, 
                  showing off the stop words filtration asking."""
    output = filter_sentence(example_sent)
    print(output) 