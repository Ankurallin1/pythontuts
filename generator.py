
"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""
"""
when we run for loop the it will print the data at runtime it doesn't store it 
whereas in case of generators it store all the value before the run of program.

yield - yield is a keyword in Python that is used to return from a function
        without destroying the states of its local variable and when the function is called, 
        the execution starts from the last yield statement. 
        Any function that contains a yield keyword is termed as generator.
Iterable - Iterables are objects that can be placed inside a loop and are capable of 
           returning one variable at a time. In simple terms, we can say that 
           iterables are objects capable of iteration. 
           Examples of iterable include list, string, tuple, etc.
           For ex. 
               for c in a:
               print (a)
               #Here a is an iterable.
Iterations - An iteration can be defined as an object that does iterations on iterable. 
             Meaning that it will move from character to character doing iteration. 
             Every iterable, either it is a string or tuple has a 
             built-in method __iter__() that creates an object when called. 
             The object moves from character to character of iterable using the 
             __next__() method. The __next__() method is, what's really behind 
             the working of the loop. 
"""
def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = "Ankur"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
