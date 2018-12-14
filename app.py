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
import time
import numpy as np
from random import *

app = Flask(__name__)
app.debug = True
sockets = Sockets(app)

x = np.arange(0,np.pi*10,0.1).tolist()

y = np.random.randint(1,100,len(x)).tolist()
print(len(x),len(y))

data_size = len(x)
counter = 0
graph_size = 100

samples = 0
tic = time.time()
def get_graph_data():

    global counter,data_size,graph_size,x,y
    global samples,tic

    #Calculate FPS
    samples += 1
    if (time.time() - tic) > 2:
        print ("FPS is : ",samples /(time.time() - tic))
        samples = 0
        tic = time.time()

    counter += 1
    if counter > (data_size - graph_size):
        counter = 0

    graph_to_send = json.dumps({
        'x':x[counter:counter+graph_size],
        'y':y[counter:counter+graph_size]
    })
    print(graph_to_send)
    return graph_to_send

# temp_c = 0
# # Logging temp data
# def log_temp(name):
#     print("Starting " + name)
#     while True:
#         global temp_c
#         gevent.sleep(1)
#         temp_c = temp_c + 1000 # real sensor reading will go here.
#         print("Temp " + str(temp_c))
#
# humidity_c = 0
# # Logging humidity data
# def log_humidity(name):
#     print("Starting " + name)
#     while True:
#         global humidity_c
#         gevent.sleep(1)
#         humidity_c = humidity_c + 1 # real sensor reading will go here.
#         print("Humidity " + str(humidity_c))



@sockets.route('/time')
def time_socket(ws):
    """ Handler for websocket connections that constantly pushes
        the latest data.
    """
    while True:
        global humidity_c, temp_c
        gevent.sleep(0.2)
        # data = json.dumps({'temp': temp_c, 'humidity': humidity_c, 'time': datetime.datetime.now().isoformat()})
        ws.send(get_graph_data())



@app.route('/')
def hello():
    """ Render our default template
    """
    return render_template('home.html')

if __name__ == "__main__":
    # Create two threads as follows
    try:
       # th1 = threading.Thread(target=log_temp, args=("temp_logger",))
       # th2 = threading.Thread(target=log_humidity, args=("humidity_logger",))
       # th1.start()
       # th2.start()
       print ("Thread(s) started..")
    except:
        print ("Error: unable to start thread")
    else:
        server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
        server.serve_forever()
