def sieve_of_eratosthenes(limit):
    """Return a list of all prime numbers less than the given limit."""
    if limit <= 2:
        return []

    # Initialize a boolean array to track prime numbers
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            # Mark multiples of num as non-prime
            for multiple in range(num * num, limit, num):
                is_prime[multiple] = False

    # Collect all prime numbers
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

# Example usage
limit = 50  # Change this value to find primes less than a different number
primes = sieve_of_eratosthenes(limit)
print(f"Primes less than {limit}: {primes}")