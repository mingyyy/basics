
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


if __name__ == '__main__':
    print(selection_sort([3,1,10,23]))