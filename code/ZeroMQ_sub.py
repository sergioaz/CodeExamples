"""
ZeroMQ subscriber
"""
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")
socket.setsockopt_string(zmq.SUBSCRIBE, "")

while True:
    msg = socket.recv_string()
    print(f"Received: {msg}")