#Given a natural number n, find the sum of the sum-series of the first N natural number.

def sum_of_sum_series(n):
    total = 0
    for i in range(1, n + 1):
        total += (i * (i + 1)) // 2
    return total

n = int(input("Enter a natural number: "))

if n > 0:
    result = sum_of_sum_series(n)
    print("Sum of sum-series for first", n, "natural numbers is:", result)
else:
    print("Please enter a positive natural number.")