
class Employee:
    no_of_leaves = 8
    var=10
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)
#inheriting class employee
class player:
    no_of_games=4
    var=5
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"
#derived will give prioty to the first parent class here Employee

class coolprogrammer(Employee,player):
    language="python"
    def printlang(self):
        print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
shubham=player("shubham","cricket")
#since the parent class of coolprogrammer have constructor which take
#arguments so we can't left coolprogrammer's parameter as empty
karan=coolprogrammer("karan",23333,"coolprogrammer")
#coolprogrammer's object is lean to intialize only first
#inherited class datamembers here it is employee
# det=karan.printdetails()
# print(karan.language)
# print(det)
print(karan.var)



