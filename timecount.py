num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
i=lcm=1
while num1%i!=1 and num2%i!=1 :
    if(num1%i==0) or (num2%i==0):
        lcm=lcm*i
    else:
        i=i+1
print(lcm)