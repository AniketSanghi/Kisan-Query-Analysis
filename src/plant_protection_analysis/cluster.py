from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

def train(documents):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(documents)

    true_k = 10
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)
    

    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(true_k):
        print("Cluster %d:" % i),
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind]),
        print
    print("\n")
    
    return model, vectorizer

def test(model, vectorizer, sentence):
    print("Prediction")

    Y = vectorizer.transform(sentence)
    prediction = model.predict(Y)
    print(prediction)


if __name__ == '__main__':
    documents = ["This little kitty came to play when I was eating at a restaurant.",
                "Merley has the best squooshy kitten belly.",
                "Google Translate app is incredible.",
                "If you open 100 tab in google you get a smiley face.",
                "Best cat photo I've ever taken.",
                "Climbing ninja cat.",
                "Impressed with google map feedback.",
                "Key promoter extension for Google Chrome."]
    model, vectorizer = train(documents)

    sentence = ["chrome browser to open."]
    test(model, vectorizer, sentence)