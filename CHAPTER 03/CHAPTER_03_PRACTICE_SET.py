# write a python program to display a user entered name followed by "Good Afternoon" using input() function 
name = input("Enter your name: ")
print("Good Afternoon " + name)


# write a program to fill in a letter template given below with name and date
# letter = '''Dear <|NAME|>,
#                   You are selected!
#                   Date: <|DATE|>''' 
NAME = input("Enter your name: ")
DATE = input("Enter date: ")
letter = '''Dear <|NAME|>,
                  You are selected!
                  Date: <|DATE|>'''
print(letter.replace("<|NAME|>", NAME).replace("<|DATE|>", DATE))
# or
letter = '''Dear <|NAME|>,
                  You are selected!
                  Date: <|DATE|>'''
NAME = input("Enter your name: ")
DATE = input("Enter date: ")
letter = letter.replace("<|NAME|>", NAME)
letter = letter.replace("<|DATE|>", DATE)
print(letter)


# write a program to detect double spaces in a string
str = input("Enter a string: ")
double_spaces = str.find("  ")
print(double_spaces) # it will return index of first occurrence of double spaces otherwise -1


# write a program to replace the double spaces with single space in the string
str = input("Enter a string: ")
str = str.replace("  ", " ")
print(str)
#JFBNKDFJB KDF

# write a program to format the following letter using escape sequence characters
letter = "Dear Harry, This Python Course is nice. Thanks!"
formatted_letter = "Dear Harry,\n\tThis Python Course is nice.\n\t\tThanks!"
print(letter)
print(formatted_letter)