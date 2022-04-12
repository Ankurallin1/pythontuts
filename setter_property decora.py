
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

"""
A property decorator is a built-in function in Python. 
Property decorator is a pythonic way to use getters and setters 
in object-oriented programming which comes from the Python property class. 
Theoretically speaking, Python property decorator is composed of four
things, i.e. getter, setter, deleter and Doc. 
The first three are methods, and the fourth one is a docstring or comment.
"""
#after using property decorator func are called without parenthesis
"""
In Oop, the setter is a very important part of the program 
as we can change the values passed in parameters easily. 

Else without a setter, it is not possible to update the values passed
as parameters during object creation. 

Setters are usually used in Oop to set the value of private attributes in a class. 
"""
hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"

print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.fname)

del hindustani_supporter.email
"""
Deleter is used to delete the values passed as a parameter before.
 
We can use a setter if we want to update or change the value, 
but we can not use it to delete the value.
 
This is where deleter comes in; 
it removes the previous value and sets the variable equal to none. 

As in Oop we do not completely erase the existence 
of some variable but sets it equal to none.
"""
print(hindustani_supporter.email)
hindustani_supporter.email = "Harry.Perry@codewithharry.com"
print(hindustani_supporter.email)

