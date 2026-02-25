# Given a number x, determine whether the given number is Armstrong's number or not. 
# A positive integer of n digits is called an Armstrong number of order n (order is the number of digits) if
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

def is_armstrong(x):
    num = x
    n = len(str(x))      # number of digits
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** n
        num //= 10

    return total == x


# User Input
x = int(input("Enter a number: "))

if is_armstrong(x):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")