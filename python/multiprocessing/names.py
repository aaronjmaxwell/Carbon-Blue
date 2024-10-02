"""Using names.

Each spawned process has a name attribute that can be changed upon
creation using the name kwarg. Naming helps to keep track of processes,
although they possess defaults. We can either name by passing using *args
or by setting an attribute once instantiated.
"""
import multiprocessing as mp
import time

import workers
import services


if (__name__ == "__main__"):
    service = mp.Process(name="my_service", target=services.lazy,)
    worker1 = mp.Process(target=workers.sleepy, args=(2, True, False),)
    worker1.name = "worker 1"
    worker2 = mp.Process(target=workers.sleepy, args=(2, True, False),)
    worker1.start()
    worker2.start()
    service.start()
