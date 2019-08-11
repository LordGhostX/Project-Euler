"""Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# My attempt to make this code as optimized as possible :)
limit = 20

# Making sure the starting number is even
curr_num = limit - (limit % 2)

# We don't need to check every number from 0 - limit when we can only check true divisors; if 2 will enter 20 there is no need to check 2 and 20, we can check only 20 and 2 will be valid
sanitized_set = list(range(2, limit + 1))
for _ in sanitized_set[::-1]:
    for __ in sanitized_set:
        if _ % __ == 0 and __ in sanitized_set and __ != _:
            sanitized_set.remove(__)

while True:
    valid = True
    for _ in sanitized_set:
        # Check if a number meets all conditions
        if curr_num % _ != 0:
            valid = False
            break
    if valid:
        break
    else:
        curr_num += 2

print(curr_num)
