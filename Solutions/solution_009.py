"""Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a b c, for which,
a
2 + b
2 = c
2
For example, 3
2 + 4
2 = 9 + 16 = 25 = 5
2
.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

limit = 1000

for i in range(1, limit + 1):
	found = False
	for j in range(1, limit + 1):
		c = ((i ** 2) + (j ** 2)) ** 0.5
		if str(c).split(".")[1] == "0" and len(str(c).split(".")[1]) == 1:
			if i + j + c == 1000:
				a, b, c = i, j, int(c)
				found = True
				break
	if found:
		break

print("{} {} {}".format(a, b, c))
