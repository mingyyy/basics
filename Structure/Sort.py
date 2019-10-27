def bubble_short(array):
    # bubble sort: going through the list and compare two items adjacent to each other.
    n = len(array)
    if n <= 1:
        return array
    counter = 1
    while counter > 0:
        counter = 0
        for i in range(n-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i + 1] = temp
                counter += 1
    return array


def selection_sort(array):
    # pointer = first item, moving the pointer to the right, pointer to be swapped to the min
    # pointer then swapped with the first item.
    # pointer moving to the second item....
    n = len(array)
    if n <= 1:
        return array
    for i in range(n):
        pointer = (i, array[i])
        for j in range(i+1, n):
            if pointer[1] > array[j]:
                pointer = (j, array[j])
        if pointer[1] < array[i]:
            array[pointer[0]] = array[i]
            array[i] = pointer[1]
    return array


def insert_sort(array):
    # starting from second item, compare with the one on the left, swap if necessary.
    # move to third item, and move to the right insert to the right place...
    n = len(array)
    if n <= 1:
        return array
    for i in range(1, n):
        marker = (i, array[i])
        j = i-1
        while j >= 0:
            if marker[1] < array[j]:
                array[marker[0]] = array[j]
                array[j] = marker[1]
                marker = (j, array[j] )
            j -= 1
    return array


def merge_sort(array):
    # merge sort, breaking into halves ...
    # add to new list based on comparison
    n = len(array)
    if n <= 1:
        return array

    middle = n//2 - 1
    left_start, left_end = 0, middle
    right_start, right_end = left_end + 1, n-1

    while left_start==left_end and right_start==right_end:
        left = merge_sort(array[left_start, left_end+1])
        right = merge_sort(array[right_start, right_end + 1])
        merge(left, right)


def merge(array_left, array_right): # TODO
    l = []
    nl = len(array_left)
    nr = len(array_right)

    for i in array_left:

        for j in array_right:
            if i > j:
                l.append(j)
            else:
                l.append(i)

import random
def quick_sort(array): # TODO
    # def swap(array, i, j):
    #     array[i], array[j]=array[j], array[i]

    def sorting(array, pivot_i):
        left, right = pivot_i, 0
        counter = 0
        for i in range(0, len(array)):
            if array[i] <= array[pivot_i]:
                left = i
            else:
                right = i

            if left > right and array[left]<array[right]:
                array[left], array[right]=array[right], array[left]
                left, right = right, left
                counter += 1
        return counter
    counter = 1
    i=1
    while counter > 0:
        pivot_i = random.choice([0,1,2,3,4])
        counter = sorting(array, pivot_i)
        i += 1
    return array


def counting_sort(array):
    # useful if the range of numbers in the list is small
    n=10
    count_list = [0]*n
    for i in array:
        count_list[i] += 1

    # accumulate
    i=1
    while i < n:
        count_list[i] += count_list[i-1]
        i += 1
    # print(count_list)
    ll = [0]*len(array)
    for i in array:
        count_list[i] -= 1
        ll[count_list[i]] = i
    return ll


from math import floor
def bucket_sort(array):
    # create n buckets
    n = 10
    bucket = [0]*n
    for i in range(len(array)):
        j = floor(array[i]*n)
        if bucket[j] != 0:
            bucket[j].append(array[i])
        else:
            bucket[j] = [array[i]]
    array = []
    for x in bucket:
        if x !=0:
            x=insert_sort(x)
            for i in x:
                array.append(i)
    return array



def redix_sort(array):
    # only for numbers, starting from the smallest digits to the largest
    # each stage use counting sort
    def get_pos_nums(num):
        pos_nums = []
        while num != 0:
            pos_nums.append(num % 10)
            num = num // 10
        return pos_nums

    def get_pos_nums2(num, i):
        if i > len(str(num)):
            return False
        else:
            return int(str(num)[i])

    temp = []
    pos = []
    for i in array:
        # get one's position
        pos.append(get_pos_nums2(i, -1))
    print(pos)
    # TODO need to modify counting_sort to handle list of list
    pos = counting_sort(pos)



if __name__ == '__main__':
    # print(bubble_sort([37,2,901,5,10]))
    # print(selection_sort([3,1]))
    # print(insert_sort([]))
    # print(bubble_short([37,2,901,5]))
    # print(quick_sort([37, 2, 901, 5, 10,11]))
    # print(counting_sort([2,0,4,5,8,0,7,5]))
    # print(bucket_sort([0.21, 0.3, 0.4, .55, .48, 0.27, .75, .85]))
    print(redix_sort([37, 23, 901, 500, 10, 119]))