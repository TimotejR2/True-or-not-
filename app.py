from flask import Flask, render_template
import time
import datetime
import datetime

# Read the date string from the file
with open('static/data/start_date.txt', 'r') as file:
    START_DATE = file.read().strip()

app = Flask(__name__)

@app.route('/')
def index():
    if datetime.datetime.now().isoformat() < START_DATE:
        return render_template('countdown.html')
        
    return render_template('homepage.html')