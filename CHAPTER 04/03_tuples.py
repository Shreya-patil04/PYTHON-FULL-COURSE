# Creating a tuple
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Accessing elements
print(tup)           # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tup[0])        # 1
print(tup[-1])       # 10

# tuple is immutable
t1 = ()
print(t1)
# t1[0] = 1  # This will raise an error

# single element tuple
# t1 = (1) : not a tuple (wrong way to create a single element tuple)
t1 = (1,)  # single element tuple
print(t1) 