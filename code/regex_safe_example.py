"""
Unsafe Regex (ReDoS Attacks)
Regex denial-of-service (ReDoS) is under-discussed in Python. A poorly written regex can chew up CPU for minutes on malicious input.

Time taken for regex match: 0.0000429 seconds
Time taken for regex match: 0.0014932 seconds
Time taken for regex match: 0.0367081 seconds
Time taken for regex match: 1.0168009 seconds
Time taken for regex match: 31.7197554 seconds

"""
import re
import time
pattern = re.compile(r"(a+)+$")
#measure the time taken to match against a malicious input
for i in [10,15, 20, 25,30]:
    start_time = time.time()
    pattern.match("a" * i + "!")
    end_time = time.time()
    print(f"Time taken for regex match: {(end_time - start_time):.7f} seconds")
# Safe alternative using re2

"""
Does not work on Windows:
"""
#import re2
#pattern = re2.compile(r"(a+)+$")
#print(pattern.match("aaaa!"))  # Safe
#safe_pattern = re2.compile(r"(?:a+)+$")

