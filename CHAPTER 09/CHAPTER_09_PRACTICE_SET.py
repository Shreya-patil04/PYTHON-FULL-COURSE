# write a program to read the text from a given file 'poems.txt'
# and find out whether it contains the word 'twinkle' or not.
f = open("C:\\Users\\Shreya Patil\\OneDrive\\Desktop\\PYTHON PROGRAMMING\\CHAPTER 09\\poems.txt", 'r')
t = f.read()
if 'twinkle' in t:
    print("yes, twinkle is present")
else:
    print("no, twinkle is not present")
f.close()


# the game() function is a program lets a user play a game and returns the score as an integer
# you need to read the file 'hisccore.txt' which you need to 
# write a program to update the hiscore whenever game() breakes the hiscore
def game():
    return 4564

score = game()
with open("hiscore.txt") as f:
    hiscoreStr = (f.read())

if hiscoreStr=='':
    with open("hiscore.txt", 'w') as f:
        f.write(str(score))

elif int(hiscoreStr)<score:
        with open("hiscore.txt", 'w') as f:
            f.write(str(score))


# write a program to generate multiplication tables from 2 to 20
# and write it to the different files.
# place these files in a folder for a 13 years old.
for i in range(2,21):
     with open(f"tables/multiplication_table_of_{i}.txt", 'w') as f:
         for j in range(1,11):
             f.write(f"{i} X {j} = {i*j}\n")
             if j!= 10:
                 f.write("\n")


# a file contains a word "donkey" multiple times. You need to write a
# program which replaces this word with "#######" by updating the same file
with open("random.txt") as f:
    content = f.read()

content = content.replace("donkey", "#######")
with open("random.txt", 'w') as f:
    f.write(content)


# repeat program 4 for a list of such words to be censored
words = ["donkey", "idiot", "stupid", "dumb"]
with open("random.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#######")

    with open("random.txt", 'w') as f:
        f.write(content)


# write a program to mime a log file and dinf out whether it contains "python"
with open("log.txt") as f:
    content = f.read()

if 'python' in content.lowe():
    print("yes python is present")
else:
    print("no python is not present")



# write a program to find out the line number whwere python is present
file_name = "log.txt"
# A counter to keep track of the line number
line_number = 0
# 'with open' is a good practice because it handles closing the file for you.
with open(file_name, 'r') as f:
    # We loop through each line in the file
    for line in f:
        # For each line we read, we increase our line number counter
        line_number += 1
        # We check if the word 'python' is in the current line
        if 'python' in line:
            # If it is, we print the line number and the line itself
            print(f"Found 'python' on line: {line_number}")
            

# write a program to make a copy of a text file "this.txt"
with open("this.txt") as f:
    content = f.read()

with open("Copy.txt", 'w') as f:
    f.write(content)



# write a program to find out whether a file is identical and matches the content of another file
file1 = "copy.txt"
file2 = "this.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("files are identical")
else:
    print("files are not identical")


# write a program to wipe out the contents of a file using python
filename = "this.txt"
with open(filename, "w") as f:
    f.write("")


# write a python program to remane a file to "renamed_by_python.txt"
oldname = "rename.txt" 
newname = "renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, "w"):
    f.write(content)


import os
os.remove(oldname) #removes the old file after renaming