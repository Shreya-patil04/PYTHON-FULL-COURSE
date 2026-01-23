# for loops
l = [1, 2, 3, 4]
for item in l:
    print(item)

fruits = ["apple", "banana", "cherry", "date"]
for items in fruits:
    print(items)


# Range functions
for i in range(8):
    print(i)

for i in range(1,20,2):
    print(i)


# for loop with else condition
for i in range(10):
    print(i)
else:
    print("loop exhausted!")


# BREAK STATEMENT
for i in range(0,80):
    print(i)
    if i == 15:
        break #loop exited immediately!
else:
    print("loop exhausted!")
