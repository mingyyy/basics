'''
Youtube Python Tutorial -26.Multithreading intro
'''

import threading
import time
arr = [2,3,8,9]
t = time.time()


def calc_square(numbers):
    print('calculate square numbers')
    for n in numbers:
        time.sleep(0.2)
        print('square:', n**2)


def calc_cube(numbers):
    print('calculate cube of numbers')
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n**3)


t1 = threading.Thread(target=calc_square, args=(arr, ))
t2 = threading.Thread(target= calc_cube, args=(arr, ))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'done in {time.time()-t}')
