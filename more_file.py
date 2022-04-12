#f.tell() will give current file pointer position
#f.seek(3) will move pointer to 3 position
f=open("ankur.txt")
print(f.tell(),)
print(f.readline(),end="")
f.seek(17)
print(f.tell(),)
print(f.readline(),end="")
f.close()