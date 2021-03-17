'''
The Pool class is used to manage a fixed number of workers, where the work can be forked and
distributed independently.  The work is done via a method / function call that is invoked once per
child, and can take one list type object as an argument (multiple args must be zipped together).  
The inputs are then mapped into the pool and executed.  The maxtasksperchild parameter in Pool can
be used to reset the workers after completing n tasks, so that long-running workers do not
continually consume resources.  In the example below, because four workers are used but there are
10 tasks, the workers need to be restarted again.
'''
import multiprocessing as mp
import numpy as np
import time

def task(x):
    return 2 * x

def zipped_task(zipped):
    global q
    x, y = zipped
    return x + y + q

def start_proc():
    print('Starting', mp.current_process().name)

if (__name__ == '__main__'):
    t = time.time()
    q = 4
    inputs = list(range(10))
    zipped = zip(np.array(list(range(10))), np.array(list(range(10))) + 1)

    builtin_outputs = map(task, inputs)
    print('Built-in: ', builtin_outputs)

    ps = mp.cpu_count()
    
    pool = mp.Pool(processes = ps, initializer = start_proc)
    outputs = pool.map(task, inputs)
    pool.close() # no more tasks
    pool.join() # wrap up current tasks
    print('task Pool    :', outputs)

    pool = mp.Pool(processes = ps, initializer = start_proc, maxtasksperchild = 2)
    outputs = pool.map(zipped_task, zipped)
    pool.close()
    pool.join()
    print('zipped task pool:', outputs)

    print(time.time() - t)
