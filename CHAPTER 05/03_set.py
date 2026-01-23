sets = {1, 2, 3, 4, 5, 1}
print(sets) #notice 1 is not repeated
print(type(sets)) 


# empty set
empty_set_example = {} #this will create an empty dictionary not set
print(type(empty_set_example)) # this is dictionary not set

empty_set = set() # this will create an empty set
print(type(empty_set)) # this is set


# adding values in empty set
empty_set.add(1)
empty_set.add(2)
empty_set.add(2) # duplicate value will not be added
print(empty_set)

# adding list, dictionary to set is not possible
# empty_set.add([1,2,3]) # this will raise an error
# empty_set.add({"a":1}) # this will raise an error

# we can add tuple to set
empty_set.add((4,5,6)) #because tuples are hashable(immutable)
print(empty_set)



