def func1(st):
    return ("THe string is",st)
def fun2(n1,n2):
    return n1+n2
"""
if we import tutmain1 in tutmain2 
without main in tut1 then the terminal of tut2 
will also execute tut1 code
"""
if __name__ == '__main__':
    print(func1("sjjs"))
    print(fun2(2, 3))

