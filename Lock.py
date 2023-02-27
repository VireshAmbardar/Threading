from threading import *
from time import *

mylock= RLock()

class Bus:
    def __init__(self, available_seats, lock):
        self.available_seats = available_seats
        self.l =lock

    def reserve(self,need_seats):
        self.l.acquire()

        print("Available seats are ",self.available_seats)

        if self.available_seats>=need_seats:
            ## name of thread
            nm =current_thread().name
            print(f"{need_seats} are alocated to {nm} ")

            #update
            self.available_seats-=need_seats
        
        else:
            print(f"{need_seats} are not available")
        
        self.l.release()


## my BudClass        
b1 = Bus(50,mylock)

t1 = Thread(target=b1.reserve, args=(10,), name="fifty")
t2 = Thread(target=b1.reserve, args=(15,), name="Shades")
t3 = Thread(target=b1.reserve, args=(13,), name="Eternal")
t4 = Thread(target=b1.reserve, args=(17,), name="Any man")
t5 = Thread(target=b1.reserve, args=(5,), name="Iron")
t6 = Thread(target=b1.reserve, args=(11,), name="Americal")
