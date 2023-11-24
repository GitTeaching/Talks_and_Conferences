from flask import Flask, render_template
import requests


app = Flask(__name__)

app.config['SECRET_KEY'] = '40361900361905b5b9f99e0361905b9f'


@app.route("/", methods=['GET'])
def home():
    shows = requests.get('http://127.0.0.1:8000/').json()
    return render_template('home.html', shows=shows['all_shows'])


if __name__ == '__main__':
    app.run(debug=True)