myDict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "marks" : [85, 90, 88], # list as a value can be used
    "another_dict" : {"a":1, "b":2} # dictionary as a value can be used
}

# dictionary methods:

# dictionary.keys()
print(myDict.keys())  
        # Output: dict_keys(['name', 'age', 'city', 'marks', 'another_dict'])
print(list(myDict.keys()))  
print(type(myDict.keys()))

# dictionary.values()
print(myDict.values()) 
        #output: dict_values(['John', 30, 'New York', [85, 90, 88], {'a': 1, 'b': 2}])

# dictionary.items()
print(myDict.items())  
        #output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York'), ('marks', [85, 90, 88]), ('another_dict', {'a': 1, 'b': 2})])

# dictionary.update()
print(myDict)  
update_dict ={"age": 31, "country": "USA"}
myDict.update(update_dict)  
        # update the dictionary with another dictionary
print(myDict)  

# dictionary.get()
print(myDict.get("name"))  
        # Output: John
print(myDict.get("non_existing_key"))  #doesnot exist in dictionary
        # Output: None (does not raise an error)

# where as if we use [] for non existing key it will raise an error
# print(myDict["non_existing_key"])  
        # KeyError: 'non_existing_key'# accessing dictionary element inside dictionary
        