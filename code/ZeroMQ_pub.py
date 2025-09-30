"""
ZeroMQ, publisher
"""
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    msg = f"Update {time.time()}"
    socket.send_string(msg)
    print(f"Sent: {msg}")
    time.sleep(1)