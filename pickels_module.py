
import pickle
"""
Pickling is a process of serializing an object. 
Serializing means to store the object in the form of binary representation so 
it can be saved in our main memory. The object could be of any type. 
It could be a string, tuple, or any other sort of object that Python supports. 
The data is stored in the main memory in a file. While writing the code for pickling, 
we open the file in "wb" mode, also known as writing binary mode. So, to use the pickle module, 
we have to make a file with .pkl extension and send it in a dump() function along with the object. 
dump() is a built-in function in the Pickle module, made for pickling.
"""
#Pickling a python object
cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
file = "mycar.pkl"
fileobj = open(file, 'wb')
pickle.dump(cars, fileobj)
fileobj.close()

# file = "mycar.pkl"
# fileobj = open(file, 'rb')
# mycar = pickle.load(fileobj)
# print(mycar)
# print(type(mycar))


# pickle.loads = ?




