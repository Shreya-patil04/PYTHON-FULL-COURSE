# strings can be written in following types: -
a = 'harry'
b = "harry"
c = '''harry'''
d = "harry's"
e = 'harry"s'
f = '''harry's and harry"s'''   
print(b)
print(type(b))


# Concatenation of strings
greeting = "Good Morning"
name = " Harry"
print(greeting + name)  
c = greeting + name
print(c)


# String Slicing: -
fruit = "apple" #length = 5 hence index = 0 to 4
print(fruit[2])
print(fruit[3])

print (fruit[0:3]) # it will print from index 0 to 2 (3-1)
print(fruit[1:4]) # it will print from index 1 to 3 (4-1)
print(fruit[0:]) # it will print from index 0 to end
print(fruit[:4]) # it will print from index 0 to 3 (4-1)
print(fruit[:]) # it will print full string

# negative indexing in strings
print(fruit[-4]) # it will print p
print(fruit[-1]) # it will print e
print(fruit[-5:-1 ]) # it will print app ( -5 to -3) 
print(fruit[-4:]) # it will print pple (-4 to end)

# slicing with skip value
veg = "tomato"
sl = veg[1:4:2]
print(sl) # it will print oa (1 to 3 with skip value of 2)

sen = "tomato is a vegetable"
print(sen[0::2]) # it will print tti a eae (0 to end with skip value of 3)
