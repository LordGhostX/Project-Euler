"""Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

# Define the range of 3 digit numbers
minimum = 100
maximum = 999

maximum_palindrome = 0
max_nums = ""

for _ in range(minimum, maximum + 1):
    for __ in range(minimum, maximum + 1):
        # iterate through every combination of multiplications
        num = str(_ * __)
        if num == num[::-1] and int(num) > maximum_palindrome:
            # check if they are palindromes and greater than our max
            maximum_palindrome = int(num)
            max_nums = "{} {}".format(_, __)

print(max_nums)
