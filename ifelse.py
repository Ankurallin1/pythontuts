print("Enter your age between 1 to 70")
n=int(input())
if n<1 or n>70:
    print("plz input in range")
else :
    if n==18:
        print("you can be consider for voting")
    elif n>18:
        print("you are eligible")
    else:
        print("not eligible for voting")

