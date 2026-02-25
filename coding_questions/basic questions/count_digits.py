# Given a number n, the task is to return the count of digits in this number.

def count_digits(n):
    count = 0
    while n>0:
        n //= 10
        count += 1
    return count

# User Input
number = int(input("Enter a number: "))
result = count_digits(number)
print(f"The count of digits in {number} is: {result}")