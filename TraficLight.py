# Example 2 - Trafific light 
## if light is green print - you can go
## if light is red - stop

## color of light in t1 thread
## msgs in t2 Thread

from threading import *
from time import *
import random

e = Event()

def light():
    # light_colors =["red","green"]
    # color = random.choice(light_colors)
    while True:
        print("light is green")
        e.set() ## put value = True and send signal
        sleep(3)

        print("light is red")
        e.clear() ## again event value = Flase and stop sending signal
        sleep(5)

    #after color is selected we will send signal
    e.set() ## set flag = True #signal is sent
    

def message():
    #3 signal is received
    e.wait()

    while e.is_set():
        print("You can go")
        sleep(1)
    
        e.wait() ## as no of time events is called (clear or set) same no of time in this def also



    pass



t1 = Thread(target=light)
t2 = Thread(target=message)

t1.start()
t2.start()


