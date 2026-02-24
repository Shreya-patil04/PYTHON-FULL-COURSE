# Given an array, write a program to find the sum of values of even and odd index positions separately.

def EvenOddSum(a, n):
    even = 0
    odd = 0
    for i in range(n):
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]
    
    print ("Even index positions sum ", even)
    print ("Odd index positions sum ", odd)

arr = [4,6,8,7,9,5]
num = len(arr)
EvenOddSum(arr, num)

