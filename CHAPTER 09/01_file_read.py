# opening file:
f = open("C:\\Users\\Shreya Patil\\OneDrive\\Desktop\\PYTHON PROGRAMMING\\CHAPTER 09\\shardul.txt", 'r')
f = open("C:\\Users\\Shreya Patil\\OneDrive\\Desktop\\PYTHON PROGRAMMING\\CHAPTER 09\\shardul.txt")
    # the above line points that the the default mode for file is reading

# reading a file: -
data = f.read()
trim = f.read(3) #print only 1st 3 characters from the content
print(data)
print(trim)
f.close() #this is used to close a file

# reads 1st line
line = f.readline()
print(line)
# reads 2nd line
line = f.readline()
print(line)

f.close()