
from math import floor
from insert import insert_sort


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

if __name__ == '__main__':
    print(bucket_sort([0.21, 0.3, 0.4, .55, .48, 0.27, .75, .05]))