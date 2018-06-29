#!/usr/bin/python

import threading
import time

exitFlag = 0


class myThread(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      print "Starting " + self.name
      printer(self.name, 5, self.counter)
      print "Exit " + self.name



def printer(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()

      time.sleep(delay)
      print "%s: %s" % (threadName, time.ctime(time.time()))
      counter -=1


# class myThread(threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)  # overrides init to add additional methods
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print "Starting" + self.name
#         print_time(self.name, 5, self.counter)
#         print "Exiting" + self.name
#
#
# def print_time(threadName, counter, delay):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#
#         time.sleep(delay)
#         print "%s: %s" % (threadName, time.ctime(time.time()))
#         counter -=1
#
thread1 = myThread(1, "thread-1", 1)
thread2 = myThread(2, "thread-2", 2)

thread1.start()
thread2.start()

print "Exit main thread"


