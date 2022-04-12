# f=open("ankur.txt","w")
#a will have no of character writting in ankur.txt
# a=f.write("ankur sahi h")
# print(a)
# f.close()
f=open("ankur.txt","r+")
print(f.read())
f.write("\naaj sat h")
f.close()