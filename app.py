# Linux: python3 -m venv env , source env/bin/activate, pip3  install -r requirements.txt
# Windows: python -m venv env , .\env\Scripts\activate, pip  install -r requirements.txt

from flask import Flask, request, jsonify, render_template
import pickle
import sklearn
from flask_cors import CORS 
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from textblob import TextBlob

import nltk
from nltk import tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from operator import itemgetter
import math
stop_words = set(stopwords.words('english'))

app = Flask(__name__)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

# model = pickle.load(open('./spamdetection.pkl', 'rb'))

def split_into_lemmas(message):
    message = message.lower()
    words = TextBlob(message).words
    # for each word, take its "base form" = lemma 
    return [word.lemma for word in words]

#function to apply the count vectorizer(BOW) and TF-IDF transforms to a set of input features
def features_transform(mail):
    #get the bag of words for the mail text
    bow_transformer = CountVectorizer(analyzer=split_into_lemmas).fit(mail)
    #print(len(bow_transformer.vocabulary_))
    messages_bow = bow_transformer.transform(mail)
    #print sparsity value
    print('sparse matrix shape:', messages_bow.shape)
    print('number of non-zeros:', messages_bow.nnz) 
    print('sparsity: %.2f%%' % (100.0 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1])))
    #apply the TF-IDF transform to the output of BOW
    tfidf_transformer = TfidfTransformer().fit(messages_bow)
    messages_tfidf = tfidf_transformer.transform(messages_bow)
    #print(messages_tfidf.shape)
    #return result of transforms
    return messages_tfidf

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/predict',methods=['POST'])
def predict():
    print('in server')
    data = request.get_json()
    email = data.get('message', '')
    print(email)
    email=[email]

    email= features_transform(email)
    output = model.predict(email)
    print(output)

    if output[0]=='spam':
        return {"val": True}
    else:
        return {"val": False}

@app.route('/keywords',methods=['GET','POST'])
def generate_keywords():    
    print('---------- Generating keywords now ----------')
    data = request.get_json() or {}
    message = data.get('message', '') #'I am a graduate. I want to learn Python. I like learning Python. Python is easy. Python is interesting. Learning increases thinking. Everyone should invest time in learning'
    n = int(data.get('n', 5))
    keywords = get_top_n(message, n)
    print(keywords)
    return {"keywords":keywords}



def get_top_n(doc, n):
    # algo
    total_words = doc.split()
    total_word_length = len(total_words)
    total_sentences = tokenize.sent_tokenize(doc)
    total_sent_len = len(total_sentences)

    tf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.','')
        if each_word not in stop_words:
            if each_word in tf_score:
                tf_score[each_word] += 1
            else:
                tf_score[each_word] = 1

    tf_score.update((x, y/int(total_word_length)) for x, y in tf_score.items())

    idf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.','')
        if each_word not in stop_words:
            if each_word in idf_score:
                idf_score[each_word] = check_sent(each_word, total_sentences)
            else:
                idf_score[each_word] = 1


    idf_score.update((x, math.log(int(total_sent_len)/y)) for x, y in idf_score.items())

    tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}

    # final result
    result = dict(sorted(tf_idf_score.items(), key = itemgetter(1), reverse = True)[:n]) 
    result_array = result.keys()
    return list(result_array)

def check_sent(word, sentences): 
    final = [all([w in x for w in word]) for x in sentences] 
    sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
    return int(len(sent_len))

if __name__ == "__main__":
    app.run(debug=True)
