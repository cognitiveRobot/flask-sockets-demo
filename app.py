from flask import Flask, render_template
from flask_sockets import Sockets
from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi
import gevent.monkey
gevent.monkey.patch_all()
import gevent
import datetime
import threading
import json


app = Flask(__name__)
app.debug = True
sockets = Sockets(app)

temp_c = 0
# Logging temp data
def log_temp(name):
    print("Starting " + name)
    while True:
        global temp_c
        gevent.sleep(1)
        temp_c = temp_c + 1000 # real sensor reading will go here.
        print("Temp " + str(temp_c))

humidity_c = 0
# Logging humidity data
def log_humidity(name):
    print("Starting " + name)
    while True:
        global humidity_c
        gevent.sleep(1)
        humidity_c = humidity_c + 1 # real sensor reading will go here.
        print("Humidity " + str(humidity_c))



@sockets.route('/time')
def time_socket(ws):
    """ Handler for websocket connections that constantly pushes
        the latest data.
    """
    while True:
        global humidity_c, temp_c
        gevent.sleep(1)
        data = json.dumps({'temp': temp_c, 'humidity': humidity_c, 'time': datetime.datetime.now().isoformat()})
        ws.send(data)



@app.route('/')
def hello():
    """ Render our default template
    """
    return render_template('home.html')

if __name__ == "__main__":
    # Create two threads as follows
    try:
       th1 = threading.Thread(target=log_temp, args=("temp_logger",))
       th2 = threading.Thread(target=log_humidity, args=("humidity_logger",))
       th1.start()
       th2.start()
       print ("Thread(s) started..")
    except:
        print ("Error: unable to start thread")
    else:
        server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
        server.serve_forever()
