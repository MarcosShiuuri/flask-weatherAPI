from flask import Flask, request as rq, render_template as rt

api_id = '0f2a2229a393a9b392f70d7f8ddb227e'



app = Flask(__name__)
@app.route("/")
def homepage():
    if rq.method == 'POST':
        city = rq.form.get('city_name')
        api_params = {'q':city, 'appid':api_id, 'units':'metric', 'lang':'en_us'}
        api_url = 'http://api.openweathermap.org/geo/1.0/direct?q='+api_params
    return rt('homepage.html')