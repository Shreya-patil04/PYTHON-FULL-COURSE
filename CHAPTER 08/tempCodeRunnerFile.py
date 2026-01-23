
# write a python function to print multiplication table of a given number
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Example usage
print_table(5)