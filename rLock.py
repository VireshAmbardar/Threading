## lets suppose multiple(3) developpers are working on a project 
## and they have make 3 def function and each function has  Lock on it

from threading import *
from time import *

# l = Lock()
## if we use Lock here , then l.acquire() withh hit 2 time. and programe will got stuck.
## for cases like this we use r lock, so that we can acquire and relese multiple time
l = RLock()

## developer 1 code
def get_first_line():
    l.acquire()
    print("Print first line")
    l.release()


## developer 2 code
def get_second_line():
    l.acquire()
    print("print seconf line")
    l.release()

def main():
    l.acquire()
    get_first_line()
    get_second_line()

    l.release()

t1 =Thread(target=main)
t1.start()