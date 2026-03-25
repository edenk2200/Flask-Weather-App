# Weather Flask App

## What it does
This app receives weather data from the openweathermap API and brings it into a website using flask in python.

## Features
This web app uses flask. It allows a user to input a specific city to view its weather conditions. It will then display the following 5 weather conditions on the website:
    - City Entered
    - Temperature
    - Weather Condition
    - Humidity
    - Wind Speed


## Tech used
- Python
- Flask
- Openweathermap API
- HTML
- CSS

## Installation and usage 
1. Download the program or clone the repo.
    - git clone https://github.com/edenk2200/Flask-Weather-App
2. Install dependencies
    - pip install -r requirements.txt
3. Set up API key

    Create an environment variable:

    - Mac/Linux:
    export WEATHER_API_KEY="your_api_key"

    - Windows (PowerShell):
    setx WEATHER_API_KEY "your_api_key"
4. Run the program
    - Click "Run" in your IDE
    - or type in the terminal:
    ```
    "main.py" 
    ```
5. Open localhost:5000 in your browser after running the program.

## What I learned
1. I learnt how to use basic flask
2. I learnt how to use the Jinja2 templating engine in html
3. I learnt about "Post" and "Get" in html
4. I learnt how to do basic styling in real world contexts (In CSS)
5. I learnt how to use render_template and request modules