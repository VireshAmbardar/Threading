## import thread
from threading import *

class Animal:
    @staticmethod #no need to pass self
    # @classmethod

    def Dog(n):
        for i in range(n):
            print("Dog")


class Bird:
    @classmethod ## if u are using class method you can directly call it with out refference
    def sparrow(slef,n):
        for i in range(n):
            print("Sparrow")

##  make objects 
# ob1 = Animal()
# ob2 = Bird()

##make threads
th1 = Thread(target=Animal.Dog, kwargs={"n":5})

th2 = Thread(target=Bird.sparrow, kwargs={"n":3})


## start threads
th1.start()
th2.start()

# join
# th2.join()
# th1.join()

# print("bye")