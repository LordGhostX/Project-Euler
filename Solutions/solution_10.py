"""Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

def is_prime(n):
    for _ in range(2, int(n ** 0.5) + 1):
        # Only check to the square root of a number cos the max product for a number is sqrt * sqrt
        if n % _ == 0:
            return False
    return True and n != 1

limit = 2000000

sum_of_primes = 0

for _ in range(1, limit + 1):
    if is_prime(_):
        sum_of_primes += _

print(sum_of_primes)
