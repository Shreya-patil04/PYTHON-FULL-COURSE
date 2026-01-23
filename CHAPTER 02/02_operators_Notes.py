a = 3
b = 4
# arithmetic operators: -
print("The value of 3+4 is", 3+4)
print("The value of 3-4 is", 3-4)  
print("The value of 3*4 is", 3*4)
print("The value of 3/4 is", 3/4)
print("The value of 3//4 is", 3//4) # floor division
print("The value of 3**4 is", 3**4) # 3^4
print("The value of 3%4 is", 3%4) # modulus operator

# assignment operators
c = 34
c += 2 # c = c + 2
print(c)
c -= 2 # c = c - 2
print(c)
c *= 2 # c = c * 2
print(c)
c /= 2 # c = c / 2
print(c)

# comparison operators - return boolean values
d = (3==4) # is 3 equal to 4?
print(d)
d = (3!=4) # is 3 not equal to 4?
print(d)
d = (3>=4) # is 3 greater than or equal to 4?
print(d)
d = (3<=4) # is 3 less than or equal to 4?
print(d)
d = (3>4) # is 3 greater than 4?
print(d)
d = (3<4) # is 3 less than 4?
print(d)
d = (3 is 4) # is 3 identical to 4?
print(d)
d = (3!= 4) # is 3 not identical to 4?
print(d)

# logical operators
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))
print("The value of not bool1 is", (not bool1))
print("The value of bool1 and bool2 is", (bool1 ^ bool2)) # xor operator
print("The value of bool1 NAND bool2 is", not (bool1 and bool2)) # nand operator
print("The value of bool1 NOR bool2 is", not (bool1 or bool2)) # nor operator
print("The value of bool1 XNOR bool2 is", (bool1 == bool2)) # xnor operator

#type() function & type casting: -
num = "2345"
num = int(num) # type casting
print(type(num))
print(num+5)

