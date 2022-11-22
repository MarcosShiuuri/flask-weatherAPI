from flask import Flask, request as rq, render_template as rt
import requests

api_id = '0f2a2229a393a9b392f70d7f8ddb227e'

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def homepage():
    if rq.method == 'POST':
        city = rq.form.get('city_name')
    else:
        city = 'Brasília'
    api_url = 'https://api.openweathermap.org/data/2.5/weather?'
    api_params = {'q':city, 'appid':api_id, 'units':'metric', 'lang':'en_us'}
    r = requests.get(url=api_url, params=api_params)
    ajs = r.json()
    return rt('homepage.html', url=ajs["weather"][0]["description"].capitalize())