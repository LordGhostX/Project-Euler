"""Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of allthe multiples of 3 or 5 below 1000."""

# Traditional way
limit = 1000

sum_of_multiples = 0
for _ in range(limit):
    if _ % 3 == 0 or _ % 5 == 0:
        sum_of_multiples += _

print(sum_of_multiples)
