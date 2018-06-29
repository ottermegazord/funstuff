#!/usr/bin/python

import thread
import time

# Define a function for the thread

def print_time( threadName, delay):
    # count = 0
    while 1:
        time.sleep(delay)
        # count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))


# Threads

try:
    thread.start_new_thread(print_time, ("thread1", 1, ))
    thread.start_new_thread(print_time, ("thread5", 5, ))

except:
    print "Error: unable to start thread"

while 1:
    pass