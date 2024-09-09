#!/usr/bin/python3
"""ALX SE Prime Game"""


def sieve(n):
    """Use Sieve of Eratosthenes to find all primes up to n."""
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def isWinner(x, nums):
    """Determine the winner of the prime game"""
    if not x or not nums:
        return None

    max_num = max(nums)
    primes_up_to_max = sieve(max_num)
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = [p for p in primes_up_to_max if p <= n]
        player = 0  # 0 for Maria, 1 for Ben
        remaining_numbers = set(range(1, n + 1))

        while primes:
            # Find the next available prime
            for prime in primes:
                if prime in remaining_numbers:
                    # Remove prime and its multiples
                    to_remove = set(range(prime, n + 1, prime))
                    remaining_numbers -= to_remove
                    break
            else:
                # No more primes available to choose
                break

            primes = [p for p in primes if p in remaining_numbers]
            player = 1 - player  # switch player

        # Determine who won the round
        if player == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None

