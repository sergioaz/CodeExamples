import numpy as np
import numexpr as ne
import timeit

a = np.random.rand(1_000_000)
b = np.random.rand(1_000_000)

def numpy_expr():
    return a * np.exp(b) + 3.5 * a

def numexpr_expr():
    return ne.evaluate("a * exp(b) + 3.5 * a")

numpy_time = timeit.timeit(numpy_expr, number=100)
numexpr_time = timeit.timeit(numexpr_expr, number=100)

print(f"NumPy time: {numpy_time:.4f} seconds")
print(f"NumExpr time: {numexpr_time:.4f} seconds")
print (f"NumExpr is faster than NumPy in {numpy_time/numexpr_time:.1f} times")