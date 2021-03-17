'''
Namespaces can also be managed.  Any values added to the Namespace is visible to all clients that
receive the Namespace instance.  However, updates to the contents of mutable values, such as lists,
are not propogated automatically between clients.
'''
import multiprocessing as mp

def producer(ns, event):
    ns.value = 'Grace, Too'
    event.set()

def consumer(ns, event):
    try:
        print('Before event" {}'.format(ns.value))
    except Exception as err:
        print('Before event, error:', str(err))
    event.wait()
    print('After event: ', ns.value)

if (__name__ == '__main__'):
    mgr = mp.Manager()
    ns = mgr.Namespace()
    event = mp.Event()
    p = mp.Process(target = producer, args = (ns, event))
    c = mp.Process(target = consumer, args = (ns, event))
    c.start()
    p.start()
    c.join()
    p.join()
