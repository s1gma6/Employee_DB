class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        print(f"{self.first} {self.last}")

    def gmail(self):
        return f"{(self.first).lower()}.{(self.last).lower()}@gmail.com"

# Class instance
emp_1 = Employee('Jacob', 'Carlson', 125000)

# Calling Methods
emp_1.fullname()
print(emp_1.gmail())