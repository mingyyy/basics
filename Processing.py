'''
Youtube: Python Turotial - 27 Multiprocessing Intro
'''

import time
import multiprocessing

square_result = []

def calc_square(numbers):
    global square_result
    for n in numbers:
        time.sleep(5)
        print(f'square {n*n}')
        square_result.append(n*n)

def calc_cube(numbers):
    for n in numbers:
        time.sleep(5)
        print(f'square {n**3}')

if __name__ == '__main__':
    arr = [2,4,6,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr, ))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'result {square_result}' )
    print('Done!')