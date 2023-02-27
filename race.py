 ## race condition is bug(not tecnically bcz thare are sharing 1 commin variable)

## just like we seen in print statemnt if we are passing value to increment and decrement in two different functions then sometimes it will pass values buth threadas will 
## get values randommly and do the operations in a random fasion ..

## to tackle this we use locks-mechanism

## so to tacke this we can import locks

from threading import *

## this is how lock is defined and it has 2 imputs inside it acquire and release
## lockobject.acquire(blocking = true/False , timeout =-1)

mylock = Lock()

def add(mylock,msg):
    mylock.acquire()
    
    for i in range(5):
        print(msg)

    mylock.release()
    return

def multiply(mylock,msg):
    mylock.acquire()
    
    for i in range(5):
        print(msg)

    mylock.release()
    return

num = 4

# for i in range(5):
t1 = Thread(target=add, args=(mylock,"Hello"))
t2 = Thread(target=multiply, args=(mylock,"Bye"))
    
t1.start()
t2.start()

# t1.join()
# t2.join()
