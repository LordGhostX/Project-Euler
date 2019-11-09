"""Problem 21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

def is_amicable(n, recursive=False):
    div_sum = 0
    for _ in range(1, (n + 2) // 2):
        if n % _ == 0:
            div_sum += _

    if recursive:
        return div_sum
    else:
        return n == is_amicable(div_sum, True), div_sum

limit = 10000
all_nums = list(range(1, limit))

amicables = []
while len(all_nums) > 0:
    for _ in all_nums:
        __, ___ = is_amicable(_)
        if __:
            amicables += [_, ___]
            all_nums.remove(_)
            try:
                all_nums.remove(___)
            except:
                pass
            break
        all_nums.remove(_)

amicables = list(set(amicables))
print(sum(amicables))
