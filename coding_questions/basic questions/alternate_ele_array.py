# Given an array arr[], the task is to print every alternate element of the array starting from the first element.

def print_alternate(arr):
    for i in range(0, len(arr), 2):
        print(arr[i], end=' ')

# User Input
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    arr.append(value)
print_alternate(arr)