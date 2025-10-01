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
            # Default message if none is provided
            default_message = f"{func.__name__} is deprecated and will be removed in a future version."

            warnings.warn(
                message or default_message,
                category=DeprecationWarning,
                stacklevel=2
            )
            return func(*args, **kwargs)

        return function_wrapper

    return decorator_wrapper


# --- Usage ---

@deprecated("Please use the much faster is_prime_optimized() instead.")
def is_prime(n):
    """A slow, deprecated method to check for primality."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_optimized(n):
    """An optimized method to check for primality."""
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


# Now, when you call the old function...
print(f"Is 17 prime? {is_prime(17)}")

# ...you get a nice warning:
# C:/your/path/file.py:56: DeprecationWarning: Please use the much faster is_prime_optimized() instead.
#   print(f"Is 17 prime? {is_prime(17)}")
# Is 17 prime? True