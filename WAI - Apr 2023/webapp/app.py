from flask import Flask, jsonify, request, render_template, redirect, url_for
import pandas as pd
from random import randrange
from forms import OriginalTextForm
import requests


app = Flask(__name__)

app.config['SECRET_KEY'] = '40361900361905b5b9f99e0361905b9f'


@app.route("/", methods=['POST', 'GET'])
def home():
    form = OriginalTextForm()

    if form.generate.data:
        original_text = "Hello, how are you ? This is language detection using Machine Learning algorithms."
        form.original_text.data = str(original_text)
        return render_template('home.html', form=form, output=False)

    elif form.predict.data:
        text = {"text" : form.original_text.data}
        pred = requests.post('http://127.0.0.1:8000/predict', json=text).json()
        return render_template('home.html', form=form, output=pred)

    return render_template('home.html', form=form, output=False)


if __name__ == '__main__':
    app.run(debug=True)