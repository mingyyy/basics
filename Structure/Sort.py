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

def merge(array_left, array_right):
    l = []
    nl = len(array_left)
    nr = len(array_right)
    if nl
    for i in array_left:

        for j in array_right:
            if i > j:
                l.append(j)
            else:
                l.append(i)

# print(bubble_short([37,2,901,5,10]))
# print(selection_sort([3,1]))
# print(insert_sort([]))

# print(bubble_short([37,2,901,5]))