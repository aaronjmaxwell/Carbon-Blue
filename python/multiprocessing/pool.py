import multiprocessing as mp
import numpy as np
import time

def task(x):
    return 2 * x

def zipped_task(x, y):
    global q
    return x + y + q

def start_proc():
    print('Starting', mp.current_process().name)

if (__name__ == '__main__'):
    t = time.time()
    q = 4
    N = 10000000
    inputs = list(range(N))
    x, y = np.array(list(range(N))), np.array(list(range(N))) + 1

    builtin_outputs = map(task, inputs)
    print('Built-in: ', builtin_outputs)
    
    outputs = []
    for i in inputs:
        outputs.append(task(i))
    if (N < 20):
        print(outputs)

    outputs = []
    for X,Y in zip(x,y):
        outputs.append(zipped_task(X, Y))
    if (N < 20):
        print(outputs)

    print(time.time() - t)
