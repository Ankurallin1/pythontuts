
"""
#list in python is made through square brackets
goods=["vat","gst","cgst","sgst"]
print(goods)
print(type(goods))
print(goods[3])
"""
#slicing of list is same as string go to tut6
num=[2,9,0,4,1]
num.sort()
num.reverse()
print(num[2])
print(num)
print(max(num))
print(min(num))
print(len(num))
#append means to add number in list at the end
n=[]
n.append(2)
n.append(3)
n.append(5)
print(n)
#insert func will insert no at a given position
n.insert(1,89)
print(n)
#remove func will remove number from list
n.remove(89)
print(n)
#pop will delete last number from list
n.pop()
print(n)
#tupple is a special type of list which doesn't change () are used
tp=(1,0,7)
print(tp)
print(type(tp))
#swapping two numbers
a=9
b=7
a,b=b,a
print(a,b)