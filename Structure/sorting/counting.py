
def counting_sort(array):
    # useful if the range of numbers in the list is small
    # Time complexity O(n)
    # space complexity O(n)

    n = 10
    count_list = [0]*n
    for i in array:
        count_list[i] += 1

    # accumulate
    i = 1
    while i < n:
        count_list[i] += count_list[i-1]
        i += 1
    ll = [0]*len(array)
    for i in array:
        count_list[i] -= 1
        ll[count_list[i]] = i
    return ll


if __name__ == '__main__':
    print(counting_sort([2,0,4,5,8,0,7,5]))