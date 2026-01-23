empty_set = set()

# set.add(value)
empty_set.add(1)
empty_set.add(2)
empty_set.add(3)
empty_set.add(4)
empty_set.add(5)
empty_set.add(6)
print(empty_set)

# len(set)
print(len(empty_set))

# set.remove(value) # raises KeyError if value not found 
empty_set.remove(3)
print(empty_set)

# set.pop()
print(empty_set.pop()) # removes and returns an arbitrary element
print(empty_set)
 
# set.clear()
empty_set.clear()
print(empty_set) 

# arithmetic operations on sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# set.union({values})
    # returns a new set with elements from both sets
print(setA.union(setB))

# setA.intersection(setB)
    # returns a new set with elements common to both sets
print(setA.intersection(setB))


