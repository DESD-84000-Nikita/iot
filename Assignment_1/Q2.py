#Write a program to accept a 4 digit number and
#a. Display face value of each decimal digit
#b. Display place value of each decimal digit
#c. Display no in reverse order by changing decimal place values I

num=int(input("Enter a number :"))

d=num%10
num=num/10

c=int(num%10)
num=int(num/10)

b=num%10
num=num/10

a=int(num)

print(f"face value of each number={a} {b} {c} {d}")

print(f"place value of each decimal digit ={a*1000}+{b*100}+{c*10}+{d}")

print(f"reverse no = {d}{c}{b}{a} ")