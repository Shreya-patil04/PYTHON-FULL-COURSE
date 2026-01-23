n = int(input("Enter a number: "))
print(f"Multiplication table of {n} in reverse order:")
# Loop from 10 down to 1
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")