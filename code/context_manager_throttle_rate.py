"""
Use Case #2: API Rate Limiting (Don’t Get Banned, Please)
If you’re scraping or pinging APIs, you know the fear:
“Too many requests. Try again later.”

Let’s build a smart delay:
"""
import time
from contextlib import contextmanager

@contextmanager
def throttle(seconds):
    yield
    time.sleep(seconds)

for _ in range(5):
    with throttle(1):  # Pause 1 second between calls
        ping_api()