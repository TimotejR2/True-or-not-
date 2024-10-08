from flask import Flask, render_template, request, make_response
import time
import datetime
import datetime
import json

# Read the date string from the file
with open('static/data/start_date.txt', 'r') as file:
    START_DATE = file.read().strip()

app = Flask(__name__)

@app.route('/')
def index():
    if datetime.datetime.now().isoformat() < START_DATE:
        return render_template('countdown.html')
        
    return render_template('homepage.html')

@app.route('/qr', methods=['GET'])
def qr_scaned():
    with open('config/pages.json', 'r') as file:
        code = request.args.get('code')
        data = file.read()
        pages = json.loads(data)['pages']
        for page in pages:
            if page['code'] == code:
                resp = make_response(render_template('qr_scaned.html', **page))
                resp.set_cookie('code', code, samesite='Lax')
                return resp
        
    
    return render_template('qr.html')