#!/usr/bin/env python3
#test

#import light python script contains LED code.
import light
import os
#import flask server stuff.
from flask import *

import time
import random

#create Flask app and global pi 'light' object. Static folder for html pics.
app = Flask(__name__, static_url_path='/static')
pi_light = light.interlight()

#Define app routes here;


#Index route for main html page.
@app.route("/")
def index():
      temp1 = light.measure_temp()
      return render_template('index.html' , temp=temp1)

#favicon location
@app.route("/favicon.ico")
def favicon():
      return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


#LED on and off button route
@app.route('/led/<int:state>', methods=['POST'])
def led(state):
    if state == 0:
        pi_light.set_redbright(255)      #inverted for my circuit
        pi_light.set_greenbright(255)     #change these two lines for on and off / pwm. use 'led' instead of 'bright'.
        pi_light.set_greenbright(255)
    else:
       return ('Unknown LED state!', 400)
    return ('', 204)

#Route to dim RED LED channel. Reversed for my LEDs (255-)
@app.route('/red/<int:state>', methods=['POST'])
def red(state):
    pi_light.set_redbright(255-state)
    return ''  # returns nothing to remove 500 error.

#Route to dim Green LED channel. Reveresed.
@app.route('/green/<int:state>', methods=['POST'])
def green(state):
    pi_light.set_greenbright(255-state)
    return ''  # returns nothing to remove 500 error.

#Route to dim Blue LED channel. Reversed.
@app.route('/blue/<int:state>', methods=['POST'])
def blue(state):
    pi_light.set_bluebright(255-state)
    return ''  # returns nothing to remove 500 error.

#Route for temp sensor reading real time update
@app.route('/temp/')
def temp():
    def get_temp():
        while True:
            yield('Value: {0}'.format(random.randrange(0,100)))
            time.sleep(1.0)
    return Response(get_temp(), mimetype='text/event-stream')

#Start the flask debug server listening on the pi port 5000 by default:
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)


