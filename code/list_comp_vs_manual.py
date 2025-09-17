import random
import time

def gen_test(n=100):
    """Generate a test list of random integers."""
    return [random.randint(0, n) for _ in range(n)]

n = 100000000
test = gen_test()

pivot = random.choice(test)

start = time.time()
left = [ x for x in test if x < pivot ]
right = [ x for x in test if x > pivot ]
pivot_list = [ x for x in test if x == pivot ]
total1 = time.time() - start

print(f"Time taken: {total1:.7f} seconds")

# create lists manually in one pass
left = []
right = []
pivot_list = []
start = time.time()
for x in test:
    if x < pivot:
        left.append(x)
    elif x > pivot:
        right.append(x)
    else:
        pivot_list.append(x)
total2 = time.time() - start
print(f"Time taken im manual pass: {total2:.7f} seconds, manual pass is {total2/total1:.2f} times faster")
