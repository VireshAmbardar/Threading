## 3 ways
## 1 by Event Object
## 2 by Condition object
## 3rd by Queue model

## Event Object :- class Event only 2 threads not more tha 2 threads
## flag varibale 
## thread 2 waits for a signal and a contion is meet in thread 1  , flag is used to send signal

## t2 is witing by wait()

from threading import *
from time import *

## supopese t1 - start and execute  and t2 thread = will destry session

lock = RLock()
e = Event()

def task():
    # lock.acquire()
    print("Game is started ")
    sleep(5)
    
    ## condition ##right now flag = False
    e.set() # it will cahnge flag value = True

    
    # lock.release()

def end_session():
    e.wait()
    #If contition is true 

    if e.is_set(): # if event = True
        print("session is ended")
    

t1 = Thread(target=task)
t2 = Thread(target=end_session) 

t1.start()
t2.start()

