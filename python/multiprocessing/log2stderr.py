"""Logging at the module level

`multiprocessing` has a module-level function to set up a logging object
and pass it to stderr.
"""
import logging
import multiprocessing as mp

import workers


if (__name__ == '__main__'):
    mp.log_to_stderr(logging.DEBUG)
    processes = []
    for name in ["alpha", "beta", "delta", "gamma"]:
        p = mp.Process(target=workers.sleepy, args=(0.1, False, True), name=name,)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
