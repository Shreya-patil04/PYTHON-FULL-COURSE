# Given an Integer n, find the reverse of its digits.

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev


# User Input
num = int(input("Enter an integer: "))
print("Reversed number:", reverse_number(num))