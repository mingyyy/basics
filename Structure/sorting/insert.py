
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


if __name__ == '__main__':
    print(insert_sort([3,2,5,1,8,2,3,0]))