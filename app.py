import requests
from flask import Flask, render_template, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['name']

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=15670756af60911f8e0986198e435884'
        response = requests.get(url.format(city_name)).json()

        temp = response['main']['temp']
        weather = response['weather'][0]['description']
        min_temp = response['main']['temp_min']
        max_temp = response['main']['temp_max']
        icon = response['weather'][0]['icon']

        print(temp, weather, min_temp, max_temp, icon)
        return render_template('index.html', temp=temp, weather=weather, min_temp=min_temp, max_temp=max_temp,
                               icon=icon, city_name=city_name)
    else:
        return render_template('index.html')


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    return render_template("error.html", e=e), 500


if __name__ == '__main__':
    app.run(debug=True)
