'''
Locks can be used to avoid conflicting access to a single resource that is shared among multiple
processes.
'''
import multiprocessing as mp
import sys

def locked_with(lock, stream):
    with lock:
        stream.write('Lock acquired using a with statement\n')

def locked_directly(lock, stream):
    lock.acquire()
    try:
        stream.write('Lock acquired directly\n')
    finally:
        lock.release()

lock = mp.Lock()
w = mp.Process(target = locked_with, args = (lock, sys.stdout))
wo = mp.Process(target = locked_directly, args = (lock, sys.stdout))

w.start()
wo.start()
w.join()
wo.join()
