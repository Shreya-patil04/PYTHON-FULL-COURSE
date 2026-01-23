# write a program to create a dictionary of hindi words with values as
# their english translation. Provide user witha n option to look it up!
hindi_english_dict = {
    "namaste": "hello",
    "dost": "friend",
    "paani": "water",
    "khana": "food",
    "pustak": "book"
}
print("options are:", hindi_english_dict.keys())
word = input("enter the hindi word\n: ")
print("the meaning of your word is:", hindi_english_dict.get(word))


# write a program to input 8 numbers from th user and display all the unique numbers
num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
num3 = int(input("enter number 3: "))
num4 = int(input("enter number 4: "))
num5 = int(input("enter number 5: "))
num6 = int(input("enter number 6: "))
num7 = int(input("enter number 7: "))
num8 = int(input("enter number 8: "))

num_set = {num1, num2, num3, num4, num5, num6, num7, num8}
print("the unique numbers are:", num_set)


# can we have a set with 18(int) and "18"(str) as a value in it?
set1 = {18, "18"}
print(set1)


# what will be the length of the following set?
s = set()
print(len(s))
s.add(20)
print(len(s))
s.add(20.0)
print(len(s))
s.add("20")
print(len(s))


# create an empty dictionary. Allow 4 friends to enter their favourite language as values 
# and use keys as their names. Assume names are unique.
fav_lang = {}
frnd1 = input("enter your favorite language Shubham: ")
frnd2 = input("enter your favorite language Ankit: ")
frnd3 = input("enter your favorite language Rohan: ")
frnd4 = input("enter your favorite language Rahul: ")

fav_lang["Shubham"] = frnd1
fav_lang["Ankit"] = frnd2
fav_lang["Rohan"] = frnd3
fav_lang["Rahul"] = frnd4
print(fav_lang)

# if names of 2 friends are same, whart will happen to the program above?
# the value of the first friend will be replaced by the value of the second friend
# because dictionary keys are unique

# if language of 2 friends are same, what will happen?
# nothing will happen, because dictionary values can be same


# can you change the values inside a list which is contained in a set s?
s = {8, 9, 7, "shubham", (1, 2), [1, 2, 3]} 
    # this will raise an error because list is unhashable
    # /we can only add tuple in set because tuple is immutable
print(s)
