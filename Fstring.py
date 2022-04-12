# F string
#methods to insert string
me="Ankur"
#a="this is %s"%me
al=3
#a="this is %s %s"%(me,al)
# a="this is {} {}"
# b=a.format(me,al)
# print(b)
#to improve readibility we use fstring
a=f"this is {me} {al} {1*67}"
print(a)