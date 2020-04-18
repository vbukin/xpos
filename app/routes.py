from flask import render_template, request
from app import app
import time

datain = None
dataout = None


@app.route('/')
@app.route('/index')
def index():
    global datain
    return render_template('index.html', datain=datain, title='cashbox')


@app.route('/longpolling', methods=['POST'])
def longpolling():
    global datain
    global dataout

    datain = request.get_json()
    while dataout is None:
        time.sleep(0.1)
    datain = ""
    dataoutreal = dataout
    dataout = None

    return dataoutreal


@app.route('/check', methods=['GET'])
def check():
    global datain
    while datain is None:
        time.sleep(0.1)
    senddata = datain
    datain = None
    print("datain " + str(senddata))
    return senddata


@app.route('/sendcashbox', methods=['POST'])
def oauth():
    global dataout
    dataout = request.get_data()
    return ""
