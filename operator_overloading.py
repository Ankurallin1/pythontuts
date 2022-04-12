
class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    """
    Methods starting with a double underscore ( __ ) and ending with a double underscore ( __ ) represents dunder methods.
    """

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves
#plz watch the method mapping operators to functions list
    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
"""
1.If the implementation of __str__ is missing, then __repr__ function is used as a fallback. 
 If the implementation of __repr__ is missing, then there will be no fallback.
2.If __repr__ function is returning the String representation of the object, we can skip the implementation of __str__ function. 
3.The priority of __str__ is higher than __repr__.
"""
emp1 =Employee("Harry", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
print(str(emp1))
