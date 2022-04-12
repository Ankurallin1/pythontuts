#multilevel is a combination single and multiple inheritance
class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()
#if a datameber is same in all class then the the object will execute its class datamember
#else derived class .If it could'nt find the class then it will jump to superclass of its
#derived class
# print(darry.guitar)

# electronic device
# pocket gadget
# phone



