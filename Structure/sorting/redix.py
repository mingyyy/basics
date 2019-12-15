from counting import counting_sort

def redix_sort(array):
    # only for numbers, starting from the smallest digits to the largest
    # each stage use counting sort
    def get_pos_nums(num):
        pos_nums = []
        while num != 0:
            pos_nums.append(num % 10)
            num = num // 10
        return pos_nums

    def get_pos_nums2(num, i):
        if i > len(str(num)):
            return False
        else:
            return int(str(num)[i])

    temp = []
    pos = []
    for i in array:
        # get one's position
        pos.append(get_pos_nums2(i, -1))
    print(pos)
    # TODO need to modify counting_sort to handle list of list
    pos = counting_sort(pos)


if __name__ == '__main__':
    print(redix_sort([37, 23, 901, 500, 10, 119]))