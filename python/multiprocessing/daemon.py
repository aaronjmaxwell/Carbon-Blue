"""Using daemons.

By default, the main program will not exit until all child processes
have exited. By setting a multiprocess' daemon attribute, __main__ can
successfully exit even if a daemon hangs. However, upon exiting, all
daemons are destroyed. As with a process name, the daemon attribute can
be set using *args or after calling.
"""
import multiprocessing as mp
import time
import sys

import workers
import services


if (__name__ == '__main__'):
    d = mp.Process(name="daemon", target=services.demon, args=(100, True))
    d.daemon = True
    w = mp.Process(name="worker", target=workers.sleepy, args=(10, True, True), daemon=False,)
    d.start()
    time.sleep(1)
    w.start()
