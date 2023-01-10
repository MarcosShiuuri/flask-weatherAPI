from flask import Flask, request, render_template
import requests

api_id = '0f2a2229a393a9b392f70d7f8ddb227e'

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        city = request.form.get('city_name')
    else: city = 'Brasília'
    api_url = 'https://api.openweathermap.org/data/2.5/weather?'
    api_params = {'q':city, 'appid':api_id, 'units':'metric', 'lang':'en_us'}
    r = requests.get(url=api_url, params=api_params)
    ajs = r.json()
    data = {
        "name": ajs['name'],
        "desc": ajs['weather'][0]['description'],
        "temp": int(ajs['main']['temp']),
        "temp_f": int(ajs['main']['temp']*1.8+32),
        "humi": ajs['main']['humidity']
    }
    return render_template('homepage.html', data=data)

if __name__ == '__main__':
    app.run()