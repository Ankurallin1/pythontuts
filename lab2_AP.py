p=float(input("Enter the principal amount :"))
r=float(input("Enter the rate of interest :"))
t=int(input("Enter the time period :"))
n=float(input("Enter the compounding frequency per annum :"))
simp_interest=p*r*t/100
comp_interest=p*pow((1+r/n),n*t)-p
print(f"simple interest : {simp_interest}\ncompound interest : {comp_interest}")
