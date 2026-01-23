# write a program using function to find the greatest of 3 numbers:
def largest_num(num1, num2,num3):
    if(num1>num2 and num1>num3):
        return("largest number is: " + str(num1))
    elif(num2>num1 and num2>num3):
        return("largest number is: " + str(num2))
    else:
        return("largest number is: " + str(num3))

l = largest_num(3,4,5)        
print(l)


# write a program using functions to converst celsius into fahrenheit
def temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

c = float(input("Enter temperature in Celsius: "))

# Call the function and display result
f = temperature(c)
print(f"{c}°C is equal to {f:.2f}°F")


# how do you prevent a python print() function to print a new line at the end
'''
In Python, the print() function adds a newline by default. To prevent that, you can use the end parameter and set it to an empty string or any other custom ending.

Example:
print("Hello", end="")  # No newline after this
print("World")          # Cont
'''


# write a recursive function to calculate the sum of first n natural numbers
def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

num = int(input("Enter a positive integer: "))
print(f"Sum of first {num} natural numbers is: {sum_natural(num)}")


# write a python function to print first n lines of the following pattern
'''
* * *
* *
*
'''
def pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)

num = int(input("Enter the number of lines: "))
pattern(num)


# write a python function which converts inches to cms
def conversion(inch):
    cms = inch * 2.54
    return float(cms)

i = float(input("Enter the value in inches: "))
print(conversion(i))


# write a python function to remove a given word from a list and strip it at the same time
def remove_and_split(string, word):
    newStr = string.replace(word, " ")
    return newStr.split()\
    
this = "   Good Morning        " 
n = remove_and_split(this, "harry")
print(n)


# write a python function to print multiplication table of a given number
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

print_table(5)