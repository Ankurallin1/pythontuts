# def function1():
#     print("Subscribe now")
#
# func2 = function1
# del function1
# func2()
#decorator are used to assign function to another function ex line 38
#when we have to repeat a process implemented by a func than we use decorator
def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum

a = funcret(1)
print(a)
#sum,print are inbuilt function
# def executor(func):
#     func("this")
#
#
# executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")

    return nowexec

#short form to execute decorator is using @ symbol and long form is line 38
@dec1
def who_is_harry():
    print("Harry is a good boy")


# who_is_harry = dec1(who_is_harry)

who_is_harry()


