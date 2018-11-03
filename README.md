# flask-sockets-demo

* A real-time multi-threaded data transfer demo based on Flask and WebSocket. You may also check [SSE](https://github.com/cognitiveRobot/flask-sse-thread-demo) for the server sent event based demo.
Read [this](https://www.smashingmagazine.com/2018/02/sse-websockets-data-flow-http2/) to learn more about SSE and Websockets.  


#### Main Components
* Server side - Flask, WebSocket, Thread, Gevent, JSON
* Client side - WebSocket, JSON, JavaScript and Materialize

#### Prerequisites
```
Python >= 3.6
Virtualenv
```

### Installation
Plesase follow the steps below to run the demo.

```
$ git clone git@github.com:cognitiveRobot/flask-sockets-demo.git
$ python3 -m venv venv
$ souce venv/bin/activate
$ pip install -r requirments.txt
$ python app.py
```

-- if you find any issue, don't hesitate to raise that. I will reply as early as possible.

Further Reading.
* [FullstackPython](https://www.fullstackpython.com/websockets.html) 
* [FlaskSocketIO](https://flask-socketio.readthedocs.io/en/latest/) 

