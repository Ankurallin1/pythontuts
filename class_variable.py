
class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"
#objects of class can't change variables of class
print(Employee.no_of_leaves)
#__dict__ is use to get dictionary for an object or class
print(Employee.__dict__)
#if we change no_of_leaves through object than
#than the change will happen to objects only not in
#class variable
rohan.no_of_leaves = 9
print(Employee.__dict__)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)

