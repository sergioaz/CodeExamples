"""
Bloom Filter — memory-cheap membership with tradeoffs
Problem: you need to answer “have I seen this key?” across billions of keys with tiny memory and some false positives allowed.

Why it reshaped me: it taught me to accept and model errors deliberately (false positive rate), which is crucial at scale.
"""

import hashlib
import math

class BloomFilter:
    def __init__(self, n_items, fp_rate=0.01):
        self.m = -int(n_items * math.log(fp_rate) / (math.log(2)**2))  # bits
        self.k = max(1, int((self.m / n_items) * math.log(2)))       # hash functions
        self.bitarr = bytearray((self.m + 7) // 8)

    def _hashes(self, item):
        h1 = int(hashlib.sha256(item.encode()).hexdigest(), 16)
        h2 = int(hashlib.md5(item.encode()).hexdigest(), 16)
        for i in range(self.k):
            yield (h1 + i * h2) % self.m

    def add(self, item):
        for pos in self._hashes(item):
            self.bitarr[pos // 8] |= 1 << (pos % 8)

    def __contains__(self, item):
        return all(self.bitarr[pos // 8] & (1 << (pos % 8)) for pos in self._hashes(item))

# quick demo
bf = BloomFilter(n_items=1000, fp_rate=0.01)
bf.add("alice@example.com")
print("alice" in bf, "bob" in bf, "alice@example.com" in bf)