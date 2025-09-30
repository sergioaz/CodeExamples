def count_pairs_with_difference(a, k):
    """
    Find the number of pairs of integers where the difference equals k.
    
    Args:
        a: List of positive integers
        k: Target difference
    
    Returns:
        Number of pairs modulo 10^9 + 7
    """
    MOD = 10**9 + 7
    
    # Count frequency of each number
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1
    
    pairs = 0
    
    # For each unique number, check if num + k exists
    for num in freq:
        target = num + k
        if target in freq:
            # If k == 0, we need pairs from the same number
            if k == 0:
                # Number of ways to choose 2 from freq[num] items
                count = freq[num]
                pairs += (count * (count - 1)) // 2
            else:
                # Each occurrence of num can pair with each occurrence of target
                pairs += freq[num] * freq[target]
    
    return pairs % MOD

def count_pairs_with_difference2(a, k):
    res = 0
    if not a:
        return res
    a = sorted(a)
    for i in range(len(a)):
        for j in a[i+1:]:
            if (j - a[i]) == k:
                res += 1
            elif (j - a[i]) > k:
                break
    return res

def main():
    # Test cases
    test_cases = [
        # Test case 1: Basic example
        ([1, 5, 3, 4, 2], 3),
        # Test case 2: With duplicates
        ([1, 1, 2, 2], 1),
        # Test case 3: k = 0 (same numbers)
        ([1, 1, 2, 2, 3, 3], 0),
        # Test case 4: No valid pairs
        ([1, 2, 3], 10),
        # Test case 5: Large difference
        ([1, 5, 10, 15], 5)
    ]
    
    for i, (arr, k) in enumerate(test_cases, 1):
        result = count_pairs_with_difference(arr, k)
        print(f"Test case {i}:")
        print(f"Array: {arr}")
        print(f"k: {k}")
        print(f"Number of pairs: {result}")
        print("-" * 30)
    
    # create huge array of int
    arr = [0] * 100000
    from random import randint
    for i in range(len(arr)):
        arr[i] = int (randint(0, 100000))

    print (f"{len(arr)=}")

    import time
    start = time.time()
    res = count_pairs_with_difference(arr, 10)
    print (f"{res=}")
    end = time.time()
    print(f"Execution time: {end - start:.6f} seconds")
    print(f"{res=}")

    start = time.time()
    res = count_pairs_with_difference2(arr, 10)
    print(f"{res=}")
    end = time.time()
    print(f"Execution time: {end - start:.6f} seconds")
    print(f"{res=}")


if __name__ == "__main__":
    main()