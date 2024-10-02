"""All the workers to be imported after simple import."""
import time
import sys
import multiprocessing as mp


def dummy()->None:
    """A dummy worker.

    The same worker function as in the simple multiprocessing example, but
    in its own module.
    """
    print("Worker")
    return None


def sleepy(t:float, named:bool, flush:bool, msg:str="")->None:
    """A sleepy named worker."""
    p = mp.current_process()
    if named:
        print(f"starting {p.name} @ {p.pid}")
        if flush:
            sys.stdout.flush()
    if len(msg) > 0:
        print(msg)
        if flush:
            sys.stdout.flush()
    if t > 0:
        time.sleep(t)
    if named:
        print (f"exiting {p.name} @ {p.pid}")
        if flush:
            sys.stdout.flush()


class Worker(mp.Process):
    """Extending the mp.Process class."""
    def run(self):
        """Do not overloard __init__"""
        print("In {}".format(self.name))
        return 
