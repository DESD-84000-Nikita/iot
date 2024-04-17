#Write a Python function to calculate the factorial of a number.and
# The function accepts the number as an argument.

def factorial(n):
    i=1
    fact=1
    while i<=n:
       fact=fact*i
       i=i+1
        
    print(f"factorial= ",fact)


n = int(input("Enter a number: "))
factorial(n)
