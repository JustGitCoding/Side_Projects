# Task
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

n=24

if (n in range (6, 21) or n % 2 != 0):
    print('Weird')
elif n % 2 == 0:
    print('Not Weird')


# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

a = 3
b = 2
print(f'{a+b}\n{a-b}\n{a*b}')

# Task
# The provided code stub reads two integers,  and , from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.

print(f'{a//b}\n{a/b}')


# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

for i in range (0,n):
    print(f'{i**2}')