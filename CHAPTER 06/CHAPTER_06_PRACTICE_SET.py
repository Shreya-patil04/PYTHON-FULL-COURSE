# write a program to find the greatest of four numbers entered by the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if(a>=b and a>=c and a>=d):
    print("The greatest number is:", a)
elif(b>=a and b>=c and b>=d):
    print("The greatest number is:", b)
elif(c>=a and c>=b and c>=d):
    print("The greatest number is:", c)
else:
    print("The greatest number is:", d)


# write a program to find whether a student is pass or fail,
# if it requires total 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as input from the user
subject1 = int(input("Enter marks of subject 1: "))
subject2 = int(input("Enter marks of subject 2: "))
subject3 = int(input("Enter marks of subject 3: "))

total_marks = subject1 + subject2 + subject3
percentage = (total_marks / 300) * 100

if(percentage >= 40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33):
    print("The student has passed the exam")
else:
    print("The student has failed the exam")


# a spam comments is defined as a text containing the following keywords:
# "make a lot of money", "buy now", "click this", "subscribe this"
# write a program to detect these spam comments
text = input("Enter the text: ")
if("make a lot of money" in text):
    print("This is a spam comment")
elif("buy now" in text):
    print("This is a spam comment")
elif("click this" in text):
    print("This is a spam comment")
elif("subscribe this" in text):
    print("This is a spam comment")
else:
    print("This is not a spam comment")


# write a program to find whether a given username contains less than 10 characters or not
username = input("Enter the username: ")    
if(len(username) < 10):
    print("The username contains less than 10 characters")
else:
    print("The username contains 10 or more characters")


# write a program to find whether the given name is present in the list or not
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
name = input("Enter the name: ")
if(name in names):
    print("The name is present in the list")
else:
    print("The name is not present in the list")


# write a program to find whether a given number is present in a list or not
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = int(input("Enter the number: "))
if(number in numbers):
    print("The number is present in the list")
else:
    print("The number is not present in the list")


# write a program to calculate the grade of a student from his marks from the following scheme:
'''90-100 -> Ex
80-89 -> A
70-79 -> B
60-69 -> C
50-59 -> D
< 50 -> F'''
marks = int(input("Enter the marks: "))
if(marks >= 90 and marks <= 100):
    print("The grade is: Ex")
elif(marks >= 80 and marks < 90):
    print("The grade is: A")
elif(marks >= 70 and marks < 80):
    print("The grade is: B")
elif(marks >= 60 and marks < 70):
    print("The grade is: C")
elif(marks >= 50 and marks < 60):
    print("The grade is: D")
else:
    print("The grade is: F")


# write a program to find out whether a given post is talking about "harry" or not
post = input("Enter the post: ")
if("harry" in post or "Harry" in post or "HARRY" in post):
    print("The post is talking about harry")
else:
    print("The post is not talking about harry")

