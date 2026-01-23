l1 = [1, 8, 7, 6, 5, 21, 15]

# list.sort()
# print(l1.sort())   None - wrong
l1.sort()
print(l1)         # [1, 5, 6, 7, 8, 15, 21]

# list.reverse()
l1.reverse()
print(l1)         # [21, 15, 8, 7, 6, 5, 1] 

# list.append()
l1.append(100)  
print(l1)         # [21, 15, 8, 7, 6, 5, 1, 100]    

# list.insert()
l1.insert(2, 50)    
print(l1)         # [21, 15, 50, 8, 7, 6, 5, 1, 100]    

#  list.pop()
l1.pop(2)
print(l1)         # [21, 15, 8, 7, 6, 5, 1, 100]    

# list.remove()
l1.remove(100)
print(l1)         # [21, 15, 8, 7, 6, 5, 1]     

