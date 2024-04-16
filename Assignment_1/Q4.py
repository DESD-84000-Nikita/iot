a = int(input("Enter num1 : "))
b = int(input("Enter num2 : "))
c = int(input("Enter num3 : "))
 

def maximum(a, b, c): 
 
    if (a >= b) and (a >= c): 
        largest = a 
 
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
         
    return largest 
 

print(maximum(a, b, c))
 
 
 
 
 
 
 
 