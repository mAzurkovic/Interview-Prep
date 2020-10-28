class Employee:

    raise_amount = 1.04

    # This is like the constructor, when methods are created, 
    # first argument passed is instance (self) automatically.
    # Aka, self references the current instance...
    def __init__(self, first, last, pay):
        # Class attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.ca'

    # Class method to create employee name (code reusability)
    def get_name(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        # Since class variable, use Employee class name
        self.pay = self.pay * Employee.raise_amount


# Create instance of employee class
emp_1 = Employee('Amanda', 'Zurkovic', 10000000)
print(emp_1.get_name())

emp_1.apply_raise()

print(emp_1.pay)
