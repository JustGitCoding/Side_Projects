# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

n=3
if (n in range (6, 21) or n % 2 != 0):
    print('Weird')
elif n % 2 == 0:
    print('Not Weird')

# The provided code stub reads two integers from 1 to 100. Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
a = 3
b = 2
print(f'{a+b}\n{a-b}\n{a*b}')

# The provided code stub reads two integers from 1 to 100.
# Add logic to print two lines. The first line should contain the result of integer division. The second line should contain the result of float division.
# No rounding or formatting is necessary.
a = 3
b = 2
print(f'{a//b}\n{a/b}')

# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i^2.
for i in range (0,n):
    print(f'{i**2}')

# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        else:
            leap = True
    return leap

year = 2000
print(is_leap(year))


# The included code stub will read an integer, n, from STDIN.
# Without using any string methods, try to print the following:
# 123...n 
# Note that "..." represents the consecutive values in between.
n=5
for i in range(1,n+1):
    print(i,end="")

