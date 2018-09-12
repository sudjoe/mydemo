
# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

        # To get name
    def getName(self):
        return self.name

        # To check if this person is employee
    def isEmployee(self):
        return False


# Inherited or Sub class (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True

# Driver code
emp = Person("Sudhakar")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Singh") # An Object of Employee
print(emp.getName(), emp.isEmployee())
