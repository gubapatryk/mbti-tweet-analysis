from flask import Flask, render_template, request
import pickle
import sklearn
import xgboost

app = Flask(__name__)

loaded_vectorizer = pickle.load(open("vectorizer_xgb_mbti.sav", "rb"))
loaded_model = pickle.load(open("model_XGB.sav", "rb"))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prediction/', methods = ['POST', 'GET'])
def prediction():
    if request.method == 'GET':
        return f"Wyglądasz na zagubionego... Wyślij swój post w '/' aby uzyskać przewidywany typ MBTI! :)"
    if request.method == 'POST':
        prediction = predicc(request.form['Post1'])
        return render_template('prediction.html', pred = prediction)

def predicc(post):
    global loaded_vectorizer, loaded_model

    if type(post) != list:
        post = [post]

    input_vect = loaded_vectorizer.transform(post)

    return loaded_model.predict(input_vect)[0]

if __name__ == '__main__':
    app.run()
