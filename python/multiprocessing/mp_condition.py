'''
Condition objects are used to synchronize work flow so that some work can be done in parallel and
the rest done sequentially.  Stage 1 is performed, and Stage 2 is notified via condition.
'''
import multiprocessing as mp
import time

def stage_1(cond):
    name = mp.current_process().name
    print('starting ', name)
    with cond:
        print('{} done and ready for stage 2'.format(name))
        cond.notify_all()

def stage_2(cond):
    name = mp.current_process().name
    print('starting ', name)
    with cond:
        cond.wait()
        print('{} running'.format(name))

if (__name__ == '__main__'):
    condition = mp.Condition()
    s1 = mp.Process(name = 's1', target = stage_1, args = (condition,))
    clients = [mp.Process(name = 'stage_2[{}]'.format(i), target = stage_2, args = (condition,))
                for i in range(1, 3)]
    for client in clients:
        client.start()
        time.sleep(1)
    s1.start()
    s1.join()
    for client in clients:
        client.join()


