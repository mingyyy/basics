
def count_sort(array):
    # useful if the range of numbers in the list is small
    # Time complexity O(n)
    # space complexity O(n)
    minVal = min(array)
    maxVal = max(array)
    size = maxVal - minVal + 1
    count_list = [i*0 for i in range(minVal, maxVal+1)]
    for item in array:
        count_list[item - minVal] += 1

    # accumulate
    i = 1
    while i < size:
        count_list[i] += count_list[i-1]
        i += 1

    position = [i for i in range(len(array))]
    for i in array:
        count_list[i - minVal] -= 1
        position[count_list[i - minVal]] = i
    return position


if __name__ == '__main__':
    print(count_sort([2,0,4,5,9,0,7,3,1,5,7,8,9,10,30]))
    print(count_sort([9,4,10,8,2,4]))