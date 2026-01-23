story = "once upon a time in a land far, far away there lived a king and a queen"
word = "king"
# string functions: -
print(len(story)) # it will print length of string

print(story.endswith("away")) # it will return True if string ends with "away" otherwise False

print(story.count("a")) # it will return count of "a" in string  

print(word.capitalize()) # it will convert first character of string to uppercase

print(word.find("g")) # it will return index of "g" in string
print(word.find("z")) # it will return -1 if character not found in string
print(story.find("up"))

print(story.replace("king", "prince")) # it will replace "king" with "prince" in string
