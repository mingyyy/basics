import random
from math import floor
'''
divide and conquer idea
find a pivot and then recursively perform the following

1. bring the elements such that elements on the left are smaller than the pivot while elements on the right are larger
2. quicksort the left part
3. quicksort the right part
'''


def quick_sort(array):
    quick(array, 0, len(array) - 1)
    return array

def quick(array, left, right):
    if left < right:
        # pivot = last element
        pivot = array[right]
        index = partition(array, left, right, pivot)
        quick(array, left, index -1)
        quick(array, index, right)


def partition(array, left, right, pivot):
    while left < right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        if left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left


if __name__ == '__main__':
    print(quick_sort([37, 2, 90, 5, 100, 45, 50]))
    print(quick_sort([10,80,30,90,40,50,70]))
    print(quick_sort([1,7,3,15,6,8]))
