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