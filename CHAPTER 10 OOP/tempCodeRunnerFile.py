class employee:
    company = "google"
    # class attribute
    salary = 1000

harry = employee()
rohan = employee()
harry.salary = 4555
print(harry.salary)
print(rohan.salary)