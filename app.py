from flask import Flask, request, jsonify, render_template
import pickle
import sklearn
from flask_cors import CORS 
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from textblob import TextBlob


app = Flask(__name__)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

model = pickle.load(open('./spamdetection.pkl', 'rb'))

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
    

if __name__ == "__main__":
    app.run(debug=True)
