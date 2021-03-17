"""
Exit codes can be accessed by the exitcode attribute.
"""

import multiprocessing as mp
import sys
import time

def exit_error():
    sys.exit(1)


def exit_ok():
    return


def return_value():
    return 1


def raises():
    raise RuntimeError('RuntimeError')


def terminated():
    time.sleep(3)

if (__name__ == '__main__'):
    jobs = []
    funcs = [exit_error, exit_ok, return_value, raises, terminated]
    for f in funcs:
        print('starting ', f.__name__)
        j = mp.Process(target = f, name = f.__name__)
        jobs.append(j)
        j.start()
    jobs[-1].terminate()

    for j in jobs:
        j.join()
        print('{:>15}.exitcode = {}'.format(j.name, j.exitcode))
