import cProfile
import pstats
from pstats import SortKey
import random
import math

def my_function():
    result = 0
    for _ in range(1000000):  # Perform a large number of computations
        num = random.random()
        result += math.sqrt(num) * math.sin(num) / math.log(num + 1.1)
    return result


# Profile the execution of a function or script
cProfile.run('my_function()', 'profile_stats')

# Analyze the results
p = pstats.Stats('profile_stats')

# Sort by cumulative time (total time spent in a function and its callees)
p.sort_stats(SortKey.CUMULATIVE).print_stats(10)