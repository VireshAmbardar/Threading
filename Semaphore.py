## exaple - we have unioversity pubsite and we have 1000 students and  sever has 100 threads capability. it has inbuilt rLock mechnism

from threading import *
from time import *
## use BoundeedSemaphore in case of unequal no of acquire and release
s = Semaphore(3) ## default value = 1

def display(name):
    ## acquire
    s.acquire() ## acquire - deceremnt value by 1

    for i in range(5):
        print(f"Hello {name}")
        sleep(0.5)

    s.release() ## relese - increment value by 1


## creating threads
t1 = Thread(target=display,args=("thread-1",))
t2 = Thread(target=display,args=("thread-2",))
t3 = Thread(target=display,args=("thread-3",))
t4 = Thread(target=display,args=("thread-4",))
t5 = Thread(target=display,args=("thread-5",))
t6 = Thread(target=display,args=("thread-6",))
t7 = Thread(target=display,args=("thread-7",))
t8 = Thread(target=display,args=("thread-8",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()