# Given an array, the task is to determine whether an array is a palindrome or not..

def palindrome(arr, n):

    i = 0
    while i <= n // 2 and n != 0:
        if arr[i] != arr[n - i - 1]:
            print("Not Palindrome")
            return
        i += 1

    print("Palindrome")

arr = [1, 2, 3, 2, 1]
n = len(arr)
palindrome(arr, n)

# or

def palindrome(arr):
    if arr == arr[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


arr = [1, 2, 3, 2, 1]
palindrome(arr)