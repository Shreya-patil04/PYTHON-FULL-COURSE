# Given an array arr[] of positive integers, find the Mean and Median, and return the floor of both values.

import math
def mean_median(arr):
    n = len(arr)
    mean = sum(arr) / n
    mean_floor = int(mean)
    # mean_floor = math.floor(mean)

    arr.sort()
    if n % 2 == 0:
        median = (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        median = arr[n//2]

    median_floor = math.floor(median)
    return mean_floor, median_floor

# User Input
arr = list(map(int, input("Enter elements separated by space: ").split()))
mean_value, median_value = mean_median(arr)
print("Floor Mean:", mean_value)
print("Floor Median:", median_value)
