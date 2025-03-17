from socketio import Client

sio = Client()

@sio.event
def connect():
    print("Connected!")

@sio.event
def initial_data(data):
    print("Initial data:", data)

sio.connect('http://localhost:5000')  # Note: HTTP here, SocketIO upgrades to WS
sio.wait()