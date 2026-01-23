# class attributes
class Employee:
    company = "google"

harry = Employee()
rohan = Employee()
print(harry.company)
print(rohan.company)
Employee.company = "youtube"
print(harry.company)
print(rohan.company)


# instance attributes
harry.salary = 100000
rohan.salary = 200000
print(harry.salary)
print(rohan.salary)


# preference of instance attributes over class attributes
class employee:
    company = "google"
    # class attribute
    salary = 1000

harry = employee()
rohan = employee()
harry.salary = 4555
print(harry.salary)
print(rohan.salary)