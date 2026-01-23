# is operator
a = None
if(a is None):
    print("a is None")
else:
    print("a is not None")


# in operator
a = [45, 23, 67, 32, 89]
if(45 in a):
    print("45 is present in the list")
elif(100 in a):
    print("100 is present in the list")
else:
    print("100 is not present in the list")