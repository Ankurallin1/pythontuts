"""
sdknsdjksjkf
"""
print("Enter First number")
st=input()
print(st[-4::-2])

"""
comment out
"""
#print("Ankurallin1 ")
#print("Insta id","now get deleted")
"""
var=4
var2="ankur bhai rocks"
print(var)
print(type(var))
print(var2,end="\n")
print(type(var2))

print("Enter first number")
var1=input()
print("enter second number")
var2=input()
print("Sum of numbers is :",str(var1)+str(var2))

print("Enter second number")
n2=input()
print("multiplicaton of number is",int(n1)*int(n2))
"""
#print("Enter a string")
#st=input()
#print("Reverse of string is",st[::-1])
#print(len(st))
#print("First five character of string is",st[0:5])
#print("Full string",st[0:len(st)])
#print("Skipping 1 character from first five",st[0:5:2])
"""
st[0:] print full string
st[:len(st) or more than that] print full string
st[:] print full string
st[::] print full string ,second colon is for skipping the characters by default here it is 1
st[::2] will jump to every 2nd character starting from 0  till end
st[-4:-2] here -indices will be starting from the back of string 
i.e last character will be -1 second last will be -2 and so on
st[::-1] this will first reverse the string then it will jump to next character till end
st[::-2] this will first reverse the string then it will skip 1 character and jump to next
"""
"""
st="ankur is a good BoY"
print(st.isalnum()) #it will return false if there are other characters then alphabets
print(st.isalpha())#it will check alphabet and numerics only
print(st.endswith("good boy"))#check wether string ends with given string or not return in boolean
print(st.count("o"))# will print no of characters present in that string
print(st.capitalize())#first it will capitalize the first character of string and then print whole string
print(st.find("good"))#print the index value from where the search string is started
print(st.lower())#convert all character in small and print it
print(st.upper())#conver all character in capital and print it
print(st.replace("is","are"))#replace is with are in string
"""
