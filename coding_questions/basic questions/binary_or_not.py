# Given a number N, the task is to check first whether the given number is binary or not and its value should be greater than 1. 
# print true if N is the binary representation else print false.

def is_binary(num):
    if num < 0:        # negative numbers invalid
        return False
    if num == 0:       # 0 is valid binary
        return True

    while num:
        digit = num % 10
        if digit not in (0, 1):
            return False
        num //= 10
    return True


N = int(input("Enter a number: "))
print(is_binary(N))