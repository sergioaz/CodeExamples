import cProfile
import functools
import warnings

def deprecated(message=""):
    """
    A decorator to mark functions as deprecated.
    It will result in a DeprecationWarning being issued when the function is used.
    """
    def decorator_wrapper(func):
        @functools.wraps(func)
        def function_wrapper(*args, **kwargs):
            default_message = f"{func.__name__} is deprecated and will be removed in a future version."
            warnings.warn(
                message or default_message,
                category=DeprecationWarning,
                stacklevel=2
            )
            return func(*args, **kwargs)
        return function_wrapper
    return decorator_wrapper

@deprecated("is_prime is inefficient; use is_prime_optimized for better performance.")
def is_prime(n): # The old, slow function
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_optimized(n): # The new, fast function
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(limit):
    # Note: We now use the optimized function for the actual work.
    return sum(1 for i in range(limit) if is_prime(i))

def count_primes_optimized(limit):
    # Note: We now use the optimized function for the actual work.
    return sum(1 for i in range(limit) if is_prime_optimized(i))

cProfile.run("count_primes(5000)")

import pstats
profiler = cProfile.Profile()
profiler.enable()
count_primes(5000) # This will run fast now
profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats("cumulative").print_stats(5)