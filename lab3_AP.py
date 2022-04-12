x=input("Enter the list with square brackets :")
ls=[]
for i in range(len(x)):
    if x[i]=='.':
        ls.append(x[i])
    else:
        if x[i].isdigit():ls.append(int(x[i]))
print(*ls,sep=" ")
