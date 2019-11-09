"""Problem 19: Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September, April, June and November. All the rest have thirty-one, Saving February alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# first get 1 Jan 1901 day
# since 1 Jan 1900 was Monday
# then 1 Jan 1901 will be Tuesday (day++)
curr_day = 2

month_map = {"s": 30, "a": 30, "j": 30, "n": 30, "f": 28, "f-leap": 29}
months = ["j", "f", "m", "a", "may", "j", "jul", "a", "s", "o", "n", "d"]
num_sundays = 0

for year in range(1901, 2000):
    for month in months:
        try:
            if is_leap(year):
                if month == "f":
                    month_name = "f-leap"
                else:
                    month_name = "f"
            else:
                month_name = month
            days = month_map[month_name]
        except:
            days = 31

        curr_day = (curr_day + days) % 7
        if curr_day == 0:
            num_sundays += 1

print(num_sundays)
