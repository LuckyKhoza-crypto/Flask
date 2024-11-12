# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request, render_template
import urllib.request
import os
import json

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=['200 per day', '50 per hour'],
    storage_uri='memory://',
)


@app.route('/enter_location', methods=['POST', 'GET'])
def enter_location():
    if request.method == 'GET':
        return render_template('enter_location.html')
    # Retrieve location from the form
    return redirect(url_for('show_weather'))


@app.route('/show_weather')
def show_weather():

    location = request.args.get('location')
    if not location:
        location = "Seattle"

    # Get the API key from environment variable
    api_key = os.getenv('WEATHER_API_KEY')
    if not api_key:
        raise ValueError('API key not found.')

    # Define request URL for the API
    request_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{
        location}?unitGroup=us&key={api_key}&contentType=json'

    try:
        data = urllib.request.urlopen(request_url).read()
        weather_data = json.loads(data.decode('utf-8'))
    except urllib.error.URLError as e:
        f"Error fetching weather data: {e.reason}", 500
        return render_template('enter_location.html')
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

    # Render template and pass weather data
    return render_template('show_weather.html', weather_data=weather_data)


# main driver function
if __name__ == '__main__':
    # Run the application on the local development server.
    app.run(debug=True)
