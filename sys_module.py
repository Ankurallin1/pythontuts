import sys
num=5
print(sys.getsizeof(num))
num=2.5
print(sys.getsizeof(num))
num='e'
print(sys.getsizeof(num))
num=True
print(sys.getsizeof(num))
#we can seprate words in print function using sep
print("hello","world",sep="@",end="#")
#you can check all possible things that print can do
help(print)