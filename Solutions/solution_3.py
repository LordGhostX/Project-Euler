"""Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

def is_prime(n):
    for _ in range(2, int(n ** 0.5) + 1):
        if n % _ == 0:
            return False
    return True and n != 1

limit = 600851475143
multiples = [0]
for _ in range(1, int(limit ** 0.5)):
    if limit % _ == 0:
        if is_prime(_):
            multiples.append(_)

print(multiples[-1])
