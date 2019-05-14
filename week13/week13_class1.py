import flask
from flask import render_template
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

#read in the data file; make sure directory is okay!
df = pd.read_csv('SMSSpamCollection.txt', sep='\t', header=None)
#naming the columns of the data frame
df.columns = ['target', 'msg']
#assigning the columns to variables: input(x), output(y)
y = df['target']
X = df['msg']

#TfidVectorizer gets out a rarity of words; assesses importance of words --> turn emails into a matrix of numbers
cvec = TfidfVectorizer(stop_words='english', max_features = 300)
X = cvec.fit_transform(X)
#fit our model to the data
clf = MultinomialNB()
clf.fit(X, y)

df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df = df.to_html()


#starting up the flask app
app = flask.Flask(__name__)

@app.route('/table')
def table():
    return render_template('table.html', df = df)

#creating home page template
@app.route('/')
def home():
    return render_template('home.html')

#added to this url that we will be getting information from the user
@app.route('/is_spam', methods = ["GET"])
def is_spam():
    #we receive a message  --> the requesr argument that we want is a msg
        #enter url/msg = "MSG"
    msg = pd.Series(flask.request.args['msg'])
    X_new = cvec.transform(msg)
    score = clf.predict(X_new)
    results = {'prediction': score[0]}
    #return to the user in json format, so as a dictionary
    #we are basically building an API
    return flask.jsonify(results)



#Then type in: http://127.0.0.1:5000/is_spam?msg="[MSG]"
#ex: http://127.0.0.1:5000/is_spam?msg="givememoney"

@app.route('/page')
def page():
    with open("page.html", 'r') as form:
        return form.read()

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if flask.request.method == 'POST':
        #collect info as inputs
        inputs = flask.request.form
        #extract the name variable
        name = inputs['name']
        #repeats name 259 times
        result = (name+ " ")*259
        
        #display it back as a template called name.html
        return render_template('name.html', r = result)

#runs a check for the whole site
if __name__ == '__main__':
    app.run(debug=True)
