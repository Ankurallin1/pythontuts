
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

#calling the constructor
harry = Employee("Harry", 255, "Instructor")
#to use constructor for object harry we need to comment out its intialization
# harry=Employee()
#rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
#we can call member func using object of instance class
#print(rohan.printdetails())
print(harry.printdetails())
#print(harry.salary)