from d2 import D6
from anki import D1
gmail=[]
yahoo=[]
reddif=[]
def emailid(s):
    for i in range(len(s)):
        if s[i]=='@':
            j=i+1
            break
    if s[j]=='g':
        return 'g'
    elif s[j]=='r':
        return 'r'
    elif s[j]=='y':
        return 'y'
for i,j in D6.items():
    if(emailid(j)=='g'):
        gmail.append(i)
    elif emailid(j)=='r':
        reddif.append(i)
    elif emailid(j)=='y':
        yahoo.append(i)
print("Students having email id on the host @gamil.com are:")
for i in range(len(gmail)):
    print(gmail[i],D1[gmail[i]])
print("Students having email id on the host @reddif.com are:")
for i in range(len(reddif)):
    print(reddif[i],D1[reddif[i]])
print("Students having email id on the host @yahoo.com are:")
for i in range(len(yahoo)):
    print(yahoo[i],D1[yahoo[i]])


