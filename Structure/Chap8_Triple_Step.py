# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

from time import time
#recursive solution
def trip_steps(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return trip_steps(n-1)+trip_steps(n-2)+trip_steps(n-3)


# dynamic programming
def trip_steps_2(n):
    memoi = {}
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        if n-1 not in memoi:
            memoi[n-1] = trip_steps(n-1)
        if n-2 not in memoi:
            memoi[n-2] = trip_steps(n-2)
        if n-3 not in memoi:
            memoi[n-3] = trip_steps(n-3)
        return memoi[n-1]+memoi[n-2]+memoi[n-3]


def robot(grid):
    pass


grid = [
    [0,1,0,0],
    [0,0,0,0],
    [0,1,1,0],
    [1,0,0,0],
    [1,1,0,0]
        ]
robot(grid)


def magic(array):
    if len(array)==0:
        return None
    for i, x in enumerate(array):
        if i==x:
            return i


def powerset(array):
    sub={}
    for i in array:
        sub[i]=1




