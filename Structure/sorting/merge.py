
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

    return array


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


if __name__ == '__main__':
    print(merge_sort([37, 2, 901, 5, 10,11]))