# n! = 1 * 2 * 3 * 4 *........ * n
# n! = [1 * 2 * 3 * 4 *........ * (n-1)] * n
# n! = n * (n-1)!

# calculating factorial:
n = 0
product = 1
for i in range(n):
    product = product * (i+1)
print(product)

# factorial using function:
def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

f = factorial(5)
print(f)

# using recursion
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(5)
print(f)