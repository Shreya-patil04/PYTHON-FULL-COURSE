# writing in the file:
f = open("new.txt", 'w')
# f = open("C:\\Users\\Shreya Patil\\OneDrive\\Desktop\\PYTHON PROGRAMMING\\CHAPTER 09\\shardul.txt", 'r')
f.write("Please write this to file")
f.close()

# appending the file
f = open("new.txt", 'a')
f.write("I am appending the text file!")

# reading the file
f = open("new.txt", 'r')
data = f.read()
print(data)
f.close()



