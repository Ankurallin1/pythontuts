l1=["bhindi","paneer","chopsticks","aloo"]
"""
i=0
for item in l1:
    if i%2==0:
        print(f"cortana! bring {item}")
    i=i+1
"""
#enumerate function use to get index value from list etc
#above example can be written using enum
for i,item in enumerate(l1):
    if i%2==0:
        print(f"cortana! bring {item}")