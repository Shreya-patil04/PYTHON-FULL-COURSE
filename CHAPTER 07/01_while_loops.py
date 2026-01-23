# while loop
i = 0 #initialising the variable
while i< 10: #condition
    print(i) #body of the loop
    i += 1 #incrementing the variable
print("Loop ended")

i = 0
while i<7:
    print("yes " + str(i))
    i += 1
print("done") 


# infinite while loop
i = 0
while i<5:
    print(i)
    # i += 1 # this will create an infinite loop
print("Loop ended")


# write a program to print 1 to 50 using a while loop
i = 1
while i <= 50:
    print(i)
    i += 1
print("Loop ended")

# write a program to print the content of a list using while loop
list1 = [12, 34, 56, 78, 90]
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

fruits = ["apple", "banana", "cherry", "date"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1