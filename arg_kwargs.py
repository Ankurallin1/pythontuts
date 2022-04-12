def function(a,b,c,d):
    print(a,b,c,d)
#if we pass more argument than the parameters than error will be shown
#function("1","2","3","4","5")
#if we want to add more argument than more paramters are required
#to neglect this promblem we use arg and kwargs
def funargs(n,*arg,**kw):
    print(n)
    for i in arg:
        print(i)
    print("\nDictioniary")
    for key, value in kw.items():
        print(f"{key} is {value}")

ls=["ankur","gamer","codder","programmer","multi"]
#funargs(*ls)
#now if we are adding non args argument than it must pass first
#if we are not passing args than code run fine ex. funargs(non_arg)
non_arg="Coding learning"
kw={"ankur":"codder","yug":"improving","dada":"fun"}
funargs(non_arg,*ls,**kw)


