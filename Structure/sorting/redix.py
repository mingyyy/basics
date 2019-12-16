from count import count_sort

def redix_sort(array):
    # Only for numbers, starting from the least significant digits to the most
    # each stage use counting sort
    def get_pos_nums(num):
        pos_nums = []
        while num != 0:
            pos_nums.append(num % 10)
            num = num // 10
        return pos_nums

    def get_pos_nums2(num, i):
        if i > len(str(num)):
            return 0
        else:
            return int(str(num)[i])

    temp = []
    pos = []
    for i in array:
        # get one's position
        pos.append(get_pos_nums2(i, -1))
    print(pos)
    # TODO need to modify count_sort to handle list of list
    pos = count_sort(pos)


def radix_sort(array):
    m = max(array)
    i = 1
    n = 0
    # calculate the number of digits = n
    while m/i >= 1:
        n += 1
        i *= 10
        countSort(array, n)
    return n


def countSort(array, n):

    pass



if __name__ == '__main__':
    # print(redix_sort([37, 23, 901, 500, 10, 119]))
    print(radix_sort([34,1,234]))