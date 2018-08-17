# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event


__author__ = 'Freefall'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()

class RandomThread(Thread):
    def __init__(self):
        self.delay = 1
        super(RandomThread, self).__init__()

    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        print("Making random numbers")
        while not thread_stop_event.isSet():
            
            with open('stats.txt', 'r') as myfile:
                data=myfile.read().split('\n')
                print(data)
            with open('fastest.txt', 'r', encoding="utf-8") as myfile1:
                
                data1=myfile1.read().split('\n')
                if len(data1)<2:
                    data1.append("Name 1")
                    data1.append("Name 2")
                    data1.append("Name 3")                
                if len(data1)<2:
                    data1.append("Name 2")
                    data1.append("Name 3")
                if len(data1)<3:
                    data1.append("Name 3")
                print(data)          
            
            
            socketio.emit('newnumber', {'a': data[0],'b':data[1],'c':data[2],'l':data1[0],'m':data1[1],'n':data1[2]}, namespace='/test')
            
            
            sleep(self.delay)

    def run(self):
        self.randomNumberGenerator()


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = RandomThread()
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()    
    socketio.run(app)
   
