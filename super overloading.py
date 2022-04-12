class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    #if we want to access base class methods then super is used
    #if we didn't use super then the base class constructor treated as waste
    classvar1 = "I am in class B"
    #to 
    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(super().classvar1)

#here b.classvar1 is showing content in constructor self.classvar1
#because derived class object first search classvar1 in constructor of base class
#then in its attribute
a = A()
b = B()

print(b.special, b.var1, b.classvar1)
