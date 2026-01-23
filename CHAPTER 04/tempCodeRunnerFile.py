student1 = int(input("Enter marks of student 1: "))
student2 = int(input("Enter marks of student 2: ")) 
student3 = int(input("Enter marks of student 3: "))
student4 = int(input("Enter marks of student 4: "))
student5 = int(input("Enter marks of student 5: "))
student6 = int(input("Enter marks of student 6: "))

marks_list = [student1, student2, student3, student4, student5, student6]
marks_list.sort()

print("Sorted marks of students:", marks_list)