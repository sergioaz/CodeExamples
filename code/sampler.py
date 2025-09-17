"""
Reservoir Sampling — sample fairly from a stream you can’t store
Problem: you must keep a uniform random sample of k items from a stream of unknown length (logs, Kafka, telemetry). You can’t buffer everything.
"""

import random

def reservoir_sample(stream, k):
    """Return k samples from iterable stream (one-pass, O(n) time, O(k) memory)."""
    reservoir = []
    for i, item in enumerate(stream, start=1):
        if i <= k:
            reservoir.append(item)
        else:
            j = random.randrange(i)
            if j < k:
                reservoir[j] = item
    return reservoir

# example
stream = (i for i in range(1, 10_001))
print(reservoir_sample(stream, 5))