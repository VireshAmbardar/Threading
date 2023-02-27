## import thread
from threading import *
import time

videos = ["Aajio.mp4","sanam.mp4","jawa.mp4"]

## we are passsing this As a thread
class MyThread(Thread):
    ## if we describe run inside it it will overwrite run inside Thread()
    def run(self):
        for i in videos:
            print(f"{i} Started uploading...")
            time.sleep(5)
            print(f"{i} is uploded")

## this is called as a thread now

t1 = MyThread()

## if we start t1 then a run method is aldo executed which is inside Thread class
t1.start()

## this will run parallely
for i in range(10):
    time.sleep(0.3)
    print("Checking Copyright")