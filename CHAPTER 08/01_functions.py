def percent(marks):
    return ((marks[0] + marks[1] + marks[2] + marks[3] ) / 400) * 100


marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks2 = [34, 56, 98, 67]
percentage2 = percent(marks2)

print(percentage1)
print(percentage2)

# FUNCTIONS WITH ARGUMENTS: -
# write a program to greet an user with "good day" using function
def greet_name(name):
    print("Good day," + name )

greet_name("Shardul")

# DEFAULT PARAMETER VALUE:
def greet_name(name = "Shardul"):
    print("Good day," + name )

greet_name("Shreya")
greet_name()

