import json, orjson
import time

data = [{"id": i, "value": f"value-{i}"} for i in range(1_000_000)]

# json
start = time.time()
json.dumps(data)
total1 = time.time() - start
print("json:", total1)

# orjson
start = time.time()
orjson.dumps(data)
total2 = time.time() - start
print(f"orjson:{total2}, orjson is {total1/total2:.2f} times faster than json")