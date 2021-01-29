import math

class Employee:
    workingdays = 28
    company = "NetCafe"

    def __init__(self, first, last, age, work):
        self.first = first
        self.last = last
        self.age = age
        self.work = work

    def email(self):
        return (f"{self.first.lower()}.{self.last.lower()}@netmail.com")

    def fullname_(self):
        return (f"{self.first} {self.last}")

    def age_(self):
        return self.age

    def work_(self):
        return self.work
'''
#Employee details
e1 = Employee("Shivaram", "Kumar", 27, 6)
e2 = Employee("Alex", "Jack", 32, 4)
e3 = Employee("Mina", "Moorthy", 29, 5)
e4 = Employee("Mahathi", "Meghana", 36, 10)
e5 = Employee("Jyothish", "Karthik", 32, 6)

#List of employee ages
list1 = [e1.age_(),e2.age_(),e3.age_(),e4.age_(),e5.age_()]

#Usage of power function
x = 10
y = 2

print(math.pow(x, y))

#Using factorial funciton
userin = int(input("Enter number to get factorial "))
print(f"The factorial of {userin} is", math.factorial(userin))

print("")

#Using absolute value
user_ = int(input("Enter number for absolute value "))
print(f"The absolute value of {user_} is", math.fabs(user_))
'''


string = "Hello National Public School"

print(string)