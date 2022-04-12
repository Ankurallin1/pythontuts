
f1 = open("ankur.txt")

try:
    f = open("does2.txt")
#there are different types of error in python EOFError is one of the kind
except EOFError as e:
    print("Print eof error aa gaya hai", e)
# if execpt block is not running i.e no error then else part will be executed
except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")
#if there is an error or not the finally block will execute every time
finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
