#!/usr/bin/env python3
#test

#import light python script contains LED code.
import light
import os
#import flask server stuff.
from flask import *

import time

#create Flask app and global pi 'light' object. Static folder for html pics.
app = Flask(__name__, static_url_path='/static')
pi_light = light.interlight()

#Define app routes here;


#Index route for main html page.
@app.route("/")
def index():
      return render_template('index.html')


#favicon location
@app.route("/favicon.ico")
def favicon():
      return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


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
            temperature = os.popen("vcgencmd measure_temp").readline()
            yield('data: {0}\n\n'.format(temperature))
            time.sleep(1.0)
    return Response(get_temp(), mimetype='text/event-stream')

#Start the flask debug server listening on the pi port 5000 by default:
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)


