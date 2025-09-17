"""
Use Case #5: Locking Resources (Thread-Safe, Finally)
Working with threads or shared resources? This one’s gold.
No race conditions. No headaches. Just clean concurrency.
"""
import threading
from contextlib import contextmanager

lock = threading.Lock()

@contextmanager
def thread_safe():
    lock.acquire()
    try:
        yield
    finally:
        lock.release()

def update_shared_resource():
    pass


with thread_safe():
    update_shared_resource()