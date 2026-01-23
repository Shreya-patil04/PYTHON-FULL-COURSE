# write a program to print multiplication table of a given number using for loop
num = int(input("Enter the number of the table: "))
for i in range(1,11):
     print(str(num) + "x" + str(i) + "=" + str(i*num))
     # fstring
     print(f"{num} x {i} = {num*i}")


# write a program to greet all the persons names stored in a list "names" and which starts with S
names = ["Harry", "Soham", "Sachin", "Rahu"]
for items in names:
     if items.startswith("S"):
          print("Hello " + items)


# write a program to print multiplication table of a given number using while loop
num = int(input("Enter a number: "))
i = 1

# Use while loop to print the table
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1


# write a program to find whether a given number is prime or not
num = int(input("Enter a number: "))
prime = True

for i in range(2, num):
     if(num%i == 0):
          prime = False
          break

if prime: 
     print("this is a prime number")
else:
     print("this is not a prime number")


# write a program to find the sum of first n natural numbers using while loop
num = int(input("Enter a number: "))
i = 1
sum = 0
while i<= num:
     sum += i
     i += 1

print("the sum is: " + sum)


# write a program yo calculate the factorial of a given number using for loop
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num+1):
     factorial *= i

print((f"the factorial of this number is: {factorial}"))


# write a program to print multiplication table of n using for loop in reversed order
# Input from the user
n = int(input("Enter a number: "))
print(f"Multiplication table of {n} in reverse order:")
# Loop from 10 down to 1
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")