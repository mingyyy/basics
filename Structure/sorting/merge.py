def merge_sort(array):
    # merge sort, breaking into halves ...
    # add to new list based on comparison

    def mergeHalves(array, temp, leftStart, rightEnd):
        leftEnd = (rightEnd + leftStart)//2
        rightStart = leftEnd+1

        left = leftStart
        right = rightStart
        index = leftStart
        while left <= leftEnd and right <= rightEnd:
            if array[left] <= array[right]:
                temp[index] = array[left]
                left += 1
            else:
                temp[index] = array[right]
                right += 1
            index += 1
        if left > leftEnd:
            for i in range(right, rightEnd+1):
                temp[index] = array[i]
                index += 1
        else:
            for i in range(left, leftEnd+1):
                temp[index] = array[i]
                index += 1

        for i in range(leftStart, rightEnd+1):
            array[i] = temp[i]

    def merge(array, temp, leftStart, rightEnd):
        if leftStart >= rightEnd:
            return array
        middle = (leftStart + rightEnd)//2
        merge(array, temp, leftStart, middle)
        merge(array, temp, middle+1, rightEnd)
        mergeHalves(array, temp, leftStart, rightEnd)

    merge(array, [i for i in range(len(array))], 0, len(array) - 1)
    return array

if __name__ == '__main__':
    print(merge_sort([37, 2, 91, 5, 3, 4, 1, 0, 100]))