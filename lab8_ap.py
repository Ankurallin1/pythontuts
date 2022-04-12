# Write a python script to receive two numbers at run time. Add these numbers
# and print remainder when this addition is divided with the difference of
# received numbers. Use try/except clause to address possible errors.
# n1=int(input("Enter the first\n"))
# n2=int(input("enter the decond number\n"))
# try:
#     x=(n1+n2)%(n1-n2)
#     print(x)
# except ZeroDivisionError:
#     print("first and second number are same")
def spellout(str):
    from win32com.client import Dispatch
    sp = Dispatch("SAPI.SpVoice")
    sp.Speak(str)
str=input("Enter the string\n")
spellout(str)