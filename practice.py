#WAP TO GET MAX.GET MAX OF B VALUES MIN OF W VALUES.MAKE THE DIFFERENCE OF THESE TWO
#AND GET MAX OUT OF THIS THROUGH ROTATION OF ARRAY
#FOR EXAMPLE A={1,2,6,5} ROTATION OF THIS IS {5,1,2,6}
#bwbw       bbwbb
#1,2,6,5   1,8,2,9,3
#ANS=4    ANS=8
def rotate1(l):
    for i in range(len(l)):
        if i ==0:
            t=l[0]
            l[0]=l[len(l)-1]
        else:
            x=l[i]
            l[i]=t
            t=x
    return l
lsb=[]
lsw=[]
str=input("Enter the string\n")
inp=[]
result=[]
n=int(input("Enter the length\n"))
print("Enter the element")
for i in range(n):
    x=int(input())
    inp.append(x)
for j in range(n):
    lsb=[]
    lsw=[]
    for i in range(n):
        if(str[i]=='B'):
            lsb.append(inp[i])
        if str[i]=='W':
            lsw.append(inp[i])
    result.append((max(lsb)-min(lsw)))
    rotate1(inp)
print(max(result))
