#Given a natural number n, find the sum of the sum-series of the first N natural number.
def sum_of_sum_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (i * (i + 1)) // 2
    return sum

# Given a number N, the task is to check first whether the given number is binary or not and its value should be greater than 1. 
# print true if N is the binary representation else print false.
def is_binary(num):
    if num <= 1:   # covers 0, 1, and negatives
        return False
    
    while num:
        digit = num % 10
        if digit not in (0, 1):
            return False
        num //= 10
    return True

# Taking input from user
N = int(input("Enter a number: "))
print(is_binary(N))

# Given a number n, check whether it is even or odd. Return true for even and false for odd.
def even_odd(n):
    if n % 2 == 0:
        return True
    else:
        return False