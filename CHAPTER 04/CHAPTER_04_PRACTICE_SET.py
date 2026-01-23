# write a program to store seven fruits in a list entered by the user
fruit1 = input("Enter fruit 1: ")
fruit2 = input("Enter fruit 2: ")
fruit3 = input("Enter fruit 3: ")
fruit4 = input("Enter fruit 4: ")
fruit5 = input("Enter fruit 5: ")
fruit6 = input("Enter fruit 6: ")
fruit7 = input("Enter fruit 7: ")

fruit_list = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7]
print("Fruits in the list:", fruit_list)


# write a progarm to accept marks of 6 students and display them in a sorted manner
student1 = int(input("Enter marks of student 1: "))
student2 = int(input("Enter marks of student 2: ")) 
student3 = int(input("Enter marks of student 3: "))
student4 = int(input("Enter marks of student 4: "))
student5 = int(input("Enter marks of student 5: "))
student6 = int(input("Enter marks of student 6: "))

marks_list = [student1, student2, student3, student4, student5, student6]
marks_list.sort()

print("Sorted marks of students:", marks_list)


# check that a tuple cannot be changed in python
t1 = (1, 2, 3, 4, 5)
print("Original tuple:", t1)
# t1[0] = 10  # This will raise an error: 'tuple' object does not support item assignment
print("Tuple after trying to change an element (will raise error if uncommented):", t1)


# write a program to sum a list with 4 numbers
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

num_list = [num1, num2, num3, num4]
total_sum = sum(num_list)
print("Sum of the numbers in the list:", total_sum)


# write a program to count the number of zeros in a tuple
tup = (1, 0, 2, 0, 3, 0, 4, 5, 0)
zero_count = tup.count(0)
print("Number of zeros in the tuple:", zero_count)

