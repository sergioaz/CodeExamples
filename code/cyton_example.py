from scratch_111 import fast_sum
import timeit
import numpy as np

# generate array of 1000000 integers

arr = np.arange(1_000_000, dtype=np.int64)

res = fast_sum(arr)
print (f"{res=}")

t1 = timeit.timeit(lambda: fast_sum(arr), number=10)
print (f"{t1=}")

#print(timeit.timeit('res1 = fast_sum(arr)', number=1))

#print(f"{res1=}")

t2 = timeit.timeit(lambda: arr.sum(), number=10)

res = t2/t1
print(f"{t2=}, fast_sum is faster in {res:.02f} times")

#res = arr.sum()
#print (f"{res=}")

arr2 = list(range(1_000_000))
t2 = timeit.timeit(lambda: sum(arr2), number=10)

res = t2/t1
print(f"{t2=}, fast_sum is faster in {res:.02f} times")


