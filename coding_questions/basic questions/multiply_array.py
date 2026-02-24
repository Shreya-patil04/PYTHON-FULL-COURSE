# We are given an array, and we have to calculate the product of an array 
# using both iterative and recursive methods. 

# iterative method
def product_iterative(arr):
    product = 1
    for num in arr:
        product *= num
    return product

# User Input
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)
result = product_iterative(arr)
print("Product (Iterative):", result)

# recursive method
def product_recursive(arr, n):
    if n == 0:
        return 1
    return arr[n - 1] * product_recursive(arr, n - 1)

# User Input
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)
result = product_recursive(arr, len(arr))
print("Product (Recursive):", result)
