#coding=utf-8
import threading  
import random  
import time  

class Writer(threading.Thread):  
    """class using semaphore"""  

    def __init__(self,threadName,CountSem,WriteSem,AddRead):  
       
       """initialize thread"""  

       threading.Thread.__init__(self,name=threadName)  
       #self.sleepTime = random.randrange(1,6)  
       
       #set the semaphore as a data attribute of the class  
       
       self.CountSemaphore = CountSem
       self.WriteSemaphore = WriteSem
       self.AddReadSemaphore = AddRead


   
    def run(self):  
       """Print message and release semaphore"""  

       #acquire write mutex
       self.AddReadSemaphore.acquire()
       print " Thread %s  is waiting for writing!" % (self.getName()) 
       self.WriteSemaphore.acquire() 
       print " Thread %s  is writing!" % (self.getName()) 
       for i in range(1,1000):
        for j in range(1,1000):
          (i+j) % 23
       print " Thread %s  's writing finish!" % (self.getName()) 
       
       #release the  write mutex  
       self.WriteSemaphore.release()  
       self.AddReadSemaphore.release()