# l=10
# def fun(n):
#     #l=5
#     m=8
#     #local variable is unchangeble
#     global l
#     l=l+9
#     print(l,m)
#     print(n,"printed")
# fun("ankur")
#print(m)
def fun():
    x=10
    def fun2():
        global x
        x=20
    print("before",x)
    fun2()
    print("after",x)
fun()
print(x)
