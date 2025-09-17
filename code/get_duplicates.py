def get_duplicates(nums):
    """
    Returns a list of duplicate elements in the input list.

    Args:
        nums (list): List of integers.

    Returns:
        list: List of duplicate integers.
    """
    from collections import Counter

    # Count occurrences of each number
    counts = Counter(nums)

    # Filter numbers with count > 1
    duplicates = [num for num, count in counts.items() if count > 1]

    return duplicates

# create a list of 1000000 random integers between 1 and 10000
import random
nums = [random.randint(1, 100000) for _ in range(1000000)]
# check timing
import time
start = time.time()
get_duplicates(nums)
end = time.time()
print(end - start)
