# write statement
with open("new.txt", 'r') as f:
    a = f.read()
with open("new.txt", 'w') as f:
    a = f.write("me")
print(a)