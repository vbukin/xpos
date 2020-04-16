from flask import render_template, session, request, Request
from app import app
import time

datain = ""
dataout = None

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/cashbox', methods=['GET'])
def cashbox():
    global datain
    return render_template('cashbox.html', datain=datain, title='cashbox')


@app.route('/longpolling', methods=['POST'])
def longpolling():
    global datain
    global dataout

    datain = request.get_json()
    while dataout == None: time.sleep(1)
    datain = ""
    dataoutreal = dataout
    dataout = None

    return dataoutreal


@app.route('/sendcashbox', methods=['POST'])
def oauth():
    global dataout
    dataout = (request.form['dataout'])
    return render_template('index.html', title='Home')
