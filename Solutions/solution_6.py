"""Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
1
2 + 2
2 + ... + 10
2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 55
2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

limit = 100

# Generate the numbers
numbers = range(1, limit + 1)
# Find squares by applying a lambda then summing
squares_sum = sum(list(map(lambda x: x ** 2, numbers)))
# Finding all sums then squaring
sum_squares = sum(numbers) ** 2

print(sum_squares - squares_sum)
