#lamda function or anonymous function
#lamda is one line function
# minus=lambda x,y:x-y
# print(minus(8,3))
# #above statement can be written as
# def m(x,y):
#     return x-y
# print(m(2,9))
# def a_first(b):
#     return b[1]
a=[[1,14],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)