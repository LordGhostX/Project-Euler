"""Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

def is_prime(n):
    for _ in range(2, int(n ** 0.5) + 1):
        # Only check to the square root of a number cos the max product for a number is sqrt * sqrt
        if n % _ == 0:
            return False
    return True and n != 1

limit = 10001

primes = []
curr_num = 1
while len(primes) < limit:
    if is_prime(curr_num):
        primes.append(curr_num)
    curr_num += 1

print(primes[-1])
