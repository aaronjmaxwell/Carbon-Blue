'''
The event class in multiprocessing can be used to communicate state information, with an optional
timeout value.  The event can be toggled between set and unset.
'''
import multiprocessing as mp
import time

def wait_for_(event):
    '''
    Wait for the event to be set before doing anything.
    '''
    print('starting to wait for event')
    event.wait()
    print('event.is_set() -> ', event.is_set())

def wait_for_timeout(event, t):
    '''
    Wait t seconds and then timeout.
    '''
    print('starting to wait for event timeout')
    event.wait(t)
    print('timeout event.is_set() ->', event.is_set())

if (__name__ == '__main__'):
    event = mp.Event()
    wait = mp.Process(name = 'block', target = wait_for_, args = (event,))
    wait.start()
    timeout = mp.Process(name = 'non-block', target = wait_for_timeout, args = (event, 2))
    timeout.start()

    print('main is waiting before setting')
    time.sleep(3)
    event.set()
    print('main event is set.')
