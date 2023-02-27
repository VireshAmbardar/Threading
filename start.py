## import thread class
from threading import *

#Create a fucntion to run parallaly
def add(n_times,msgs):
    for i in range(n_times):
        print(msgs)
    return

def multiply(n1,n2):
    print(n1*n2)
    return

## create a object of thread
            ## fun_name/dont call
t1 = Thread(target=add, args=(5,"hello"))
##now function add is not in main thread so it's in thread t1

##pass variables using Kwargs
t2 = Thread(target=multiply, kwargs={"n1":3,"n2":4})

#Start/run thread
t1.run()
t2.start()