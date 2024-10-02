"""Terminating processes.

A hung process can be killed using the terminate method. Terminated
processes must still be joined back to main in order to give the process
manager time to update. In this example, the process is killed before it
can even start.
"""
import multiprocessing as mp

import workers

F = "{}: {} is alive? {}"


if (__name__ == '__main__'):
    p = mp.Process(target=workers.sleepy, args=(0.1, True, False))
    print(F.format("BEFORE", p.name, p.is_alive()))
    p.start()
    print(F.format("DURING", p.name, p.is_alive()))
    p.terminate()
    print(F.format("TERMINATED", p.name, p.is_alive()))
    p.join()
    print(F.format("JOINED", p.name, p.is_alive()))
