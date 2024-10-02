"""All the workers to be imported after simple import."""
import time
import sys
import multiprocessing as mp


def lazy()->None:
    """A lazy service."""
    name = mp.current_process().name
    print(f"{name} starting ...")
    time.sleep(3)
    print (f"{name} exiting ...")


def demon(t:int, flush:bool)->None:
    """A background process."""
    p = mp.current_process()
    print(f"starting {p.name} @ {p.pid}")
    if flush:
        sys.stdout.flush()
    time.sleep(t)
    if t > 10:
        print(f"we never get here because worker finishes before {p.name} @ {p.pid}")
    if flush:
        sys.stdout.flush()
