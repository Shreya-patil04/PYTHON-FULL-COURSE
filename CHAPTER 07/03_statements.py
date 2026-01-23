# CONTINUE STATEMENT
for i in range(20):
    if i == 15:
        continue #loop skips value immediately!
    print(i)
else:
    print("loop exhausted!")

# print even numbers:
for i in range(0,20):
    if i % 2 != 0:
        continue #loop skips value immediately!
    print(i)


# PASS STATEMENT
i = 4
if i>0: 
    pass #it gives no output
