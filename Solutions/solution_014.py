"""Problem 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1. Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

def collatz(n):
    def even(n):
        return n // 2
    def odd(n):
        return (3 * n) + 1

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = even(n)
        else:
            n = odd(n)
        sequence.append(n)

    return len(sequence)

max_num = 1000000
max_chain = 0
max_chain_num = 0

for _ in range(1, max_num):
    collatz_num = collatz(_)
    if collatz_num > max_chain:
        max_chain = collatz_num
        max_chain_num = _

print(max_chain_num)
