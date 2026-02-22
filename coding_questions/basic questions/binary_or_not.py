# Given a number N, the task is to check first whether the given number is binary or not and its value should be greater than 1. 
# print true if N is the binary representation else print false.

def is_binary(num):
    if num <= 1:   # reject 0, 1, and negatives as per your logic
        return False
    
    while num:
        digit = num % 10
        if digit not in (0, 1):
            return False
        num //= 10
    return True


# User input
n = int(input("Enter a number: "))

if is_binary(n):
    print(n, "is a binary number.")
else:
    print(n, "is NOT a binary number.")