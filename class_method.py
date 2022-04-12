#In this we are going to change class variable
#using object's
#For this we need to use @classmethod
class Employee:
    no_of_leaves = 8
#for constructor we use __init__ func to intialize object's instances
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
#self is treated as object of employee class ex harry,rohan
    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,leaves):
        cls.no_of_leaves=leaves
#calling the constructor
harry = Employee("Harry", 255, "Instructor")
rohan=Employee("Rohan",200,"student")
#we can call member func using object of instance class
print(rohan.printdetails())
print(harry.printdetails())
print("Before change",Employee.no_of_leaves)
#to change class variable using object
harry.change_leaves(45)
#this will change value for whole class
print("After change",Employee.no_of_leaves)