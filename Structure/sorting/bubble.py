def bubble_sort(array):
    # bubble sort: going through the list and compare two items adjacent to each other.
    # time complexity O(N**2)
    # space complexity O(1)

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


if __name__ == '__main__':
    print(bubble_sort([37,2,901,5,10,-1, 0]))