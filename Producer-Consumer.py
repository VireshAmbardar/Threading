## producer thread do some worka and push it to main thread 
## consumer threads consumes data from main thread and  we ahve to use Locsk here

## notify will wake up 1 thread

from threading import *
from time import *

## first we make a condiotn class object  asn pass lock
rlock = BoundedSemaphore()
con = Condition(rlock)


def write_data():
    con.acquire()

    with open ("report.txt", "w") as file1:
        days =["Sunday ", "Monday ","Tueday ","Wednesday "]

        for day in days:
            temp=input(f"Enter the temperature for {day}")         
            file1.write(temp + "\n")

    ## after process is done we have to notify other threads
    #  con.notify() - if only 1 thread is waiting
    con.notify_all()  #bcz more than 1 thread is waiting


    con.release()

def max_temp():
    ## acquire
    con.acquire()
    con.wait(timeout=0)

    # here we have to read
    with open("report.txt", "r") as file1:
        data = file1.readlines()
        ## reading 1 st value and removing \n
        max1 = float(data[0].strip("\n"))

        for temp in data[1:]:
            
            #24.5\n -> 24.5
            temp = float(temp.strip("\n"))

            if temp>max1:
                max1 = temp

        print(f"max Temp is {max1}")

        #release
        con.release()    

def avg_temp():
    con.acquire()
    con.wait(timeout=0)

    with open("report.txt", "r") as file1:
        data = file1.readlines()
        sum1 = 0 
        for temp in data:
            temp =float(temp.strip("\n"))
            sum1 = sum1+temp

        avg = sum1/len(data)
        print(f"Average is {avg}")
        con.release()   

prod1 = Thread(target=write_data)

cons1 = Thread(target=max_temp)
cons2 = Thread(target=avg_temp)

prod1.run()
cons1.run()
cons2.run()