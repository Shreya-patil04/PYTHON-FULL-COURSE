# creating a dictionary
myDict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "marks" : [85, 90, 88], # list as a value can be used
    "another_dict" : {"a":1, "b":2} # dictionary as a value can be used
}


# accessing values
print(myDict["name"])  # Output: John
print(myDict.get("age"))  # Output: 30
# accessing list element inside dictionary
print(myDict["marks"][1])  # Output: 90
# accessing dictionary element inside dictionary
print(myDict["another_dict"]) 
 

# mnutable
myDict["age"] = 31  # Update age
myDict["country"] = "USA"  # Add new key-value pair

# unordered
print(myDict)