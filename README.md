# Weather App with Flask and Rate Limiting

This project is a simple web application built with Flask that retrieves and displays weather information for a specified location using the Visual Crossing Weather API. It includes basic rate limiting to control the frequency of API calls.

## Features
- **Location-Based Weather Data**: Enter a location to fetch current and forecasted weather information.
- **Rate Limiting**: Limits requests to prevent excessive API usage.
- **Error Handling**: Handles common issues like missing location input or API key.

## Prerequisites
- Python 3.7 or higher
- An API key from [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api)
- Flask and other dependencies listed in `requirements.txt`

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/LuckyKhoza-crypto/Flask
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    Set up the `WEATHER_API_KEY` environment variable with your API key from Visual Crossing:
    ```bash
    export WEATHER_API_KEY=your_api_key_here
    ```

5. **Run the Application**:
    ```bash
    python app.py
    ```

6. **Access the Application**:
    Open [http://127.0.0.1:5000/enter_location](http://127.0.0.1:5000/enter_location) in your browser.

## Project Structure

- `app.py`: Main application file with route definitions.
- `templates/enter_location.html`: Template for entering a location.
- `templates/show_weather.html`: Template for displaying the weather data.
- `requirements.txt`: Lists the dependencies for the project.

## Endpoints

1. **/enter_location** (GET, POST): Accepts a location input and redirects to the weather display page.
2. **/show_weather** (GET): Retrieves and displays weather data for the specified location.

## Rate Limiting
This app uses Flask-Limiter to manage API request frequency:
- **200 requests per day**
- **50 requests per hour**

## Error Handling
- **Missing API Key**: If `WEATHER_API_KEY` is not set, the app will raise a `ValueError`.
- **Invalid Location**: If an invalid location is entered, an error will be shown on the location entry page.

Project requirements described here: https://roadmap.sh/projects/weather-api-wrapper-service

