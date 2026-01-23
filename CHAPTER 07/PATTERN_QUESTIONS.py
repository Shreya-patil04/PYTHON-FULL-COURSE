# write a program to print the star pattern
'''
*
* *
* * *
'''
num = int(input("Enter a number: "))
for i in range(num):
     print("*"*(i+1))


# write a program to print the star pattern
'''
    * 
  * * *
* * * * *
'''
num = int(input("Enter a number: "))
for i in range(num):
    # Print spaces
    for j1 in range(num - i - 1):
        print(" ", end="")
    # Print stars
    for j2 in range(i + 1):
        print("* ", end="")
    # Move to the next line
    print()


# write a program to print the star pattern
'''
* * *
*   *
* * *
'''
# Number of rows and columns
rows = 3
cols = 3

for i in range(rows):
    for j in range(cols):
        # Print star at borders
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

