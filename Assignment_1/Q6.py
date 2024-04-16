#Write a Python function to calculate the factorial of a number.and
# The function accepts the number as an argument.

def factorial(n):
    # Check if the number 'n' is 0
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Input a number to compute the factorial: "))

print(factorial(n))
