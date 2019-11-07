"""Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

NOTE: Once the chain starts the terms are allowed to go above one million.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""

def word(num):
	number_map = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 1000: "one thousand"}
	try:
		return number_map[num] #1, 2 - 12 && 1000
	except:
		if len(str(num)) == 2 and str(num)[0] == "1": #13, 14 - 19
			w = number_map[int(str(num)[1])] + "teen"
			if num == 13:
				w = w.replace("ree", "ir")
			if num == 15:
				w = w.replace("ve", "f")
			if num == 18:
				w = w.replace("tt", "t")
			return w
		if len(str(num)) == 2 and  str(num)[1] == "0": #20, 30 - 90
			w = number_map[int(str(num)[0])] + "ty"
			if num == 20:
				w = w.replace("two", "twen")
			if num == 30:
				w = w.replace("ree", "ir")
			if num == 40:
				w = w.replace("four", "for")
			if num == 50:
				w = w.replace("ve", "f")
			if num == 80:
				w = w.replace("tt", "t")
			return w
		if len(str(num)) == 2 and  str(num)[1] != "0": #1, 2 - 99
			w = word(int(str(num)[0] + "0")) + "-" + word(int(str(num)[1]))
			return w
		if len(str(num)) == 3 and  str(num)[1:] == "00": #100, 200 - 900
			w = word(int(str(num)[0])) + " hundred"
			return w
		if len(str(num)) == 3 and  str(num)[1:] != "00": #101, 102 - 999
			w = word(int(str(num)[0] + "00")) + " and " + word(int(str(num)[1:]))
			return w
		return "0"

limit = 1000

word_sum = 0

for i in range(1, limit + 1):
	word_sum += len(word(i).replace(" ", "").replace("-", ""))

print(word_sum)
