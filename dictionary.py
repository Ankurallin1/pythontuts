#dictionary is nothing but key value pairs
d1={}
#dictionary is something like we are providing words to it and in
#return it give us meaning
print(type(d1))
#we can make ans as dictionary too here like papa's ans is a dictionary
d2={"ankur":"genius","ujjwal":"topper","yug":"powerfull",
    "papa":{"b":"professional","f":"father","h":"husband"}}
print(d2["papa"]["b"])
#we can also add new words to dictionary
d2["arpit"]="funny"
print(d2)
#we can delete word using del
del d2["arpit"]
print(d2)
#now we are assigning d2 to d3
d3=d2
#here d3 is pointing to d2 so if change something in d3 then d2 will change too
del d3["ankur"]
print(d2)
#if we use d3=d2.copy() then change in d3 will not change thing in d2
d3=d2.copy()
del d3["ujjwal"]
print(d2)
#we can also update the list by adding word through following method
d2.update({"wwe":"fav"})
print(d2)
#want to print keys then use key fun
print(d2.keys())
#want to print items then use item function
print(d2.items())