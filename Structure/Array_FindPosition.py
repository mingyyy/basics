# given an ordered array (ascending) and a target value, return the position of the item if it's equal to target value,
# otherwise add it in and return position. all items in array are integers and target value is also integers.


def find_position(array, target):
    # method 1. go through the list from left to right: time O(n)
    if len(array) == 0:
        return 0
    else:
        for i in range(0, len(l)-1):
            if l[i] >= target:
                return i
            elif l[i] < target < l[i+1]:
                return i+1
            elif target == l[-1]:
                return len(l)-1
            elif target > l[-1]:
                return len(l)


def find_position_bi(array, target):
    # method 2. go through the list from middle each time
    if len(array) == 0:
        return 0
    else:
        left, right = 0, 0
        n = len(l)
        middle = (-(-n // 2)) - 1
        while left != right-1:
            # take the middle position
            if array[middle] == target:
                return middle
            elif array[middle] < target:
                left, right = middle, n-1
                middle += (-(-(right - left+1) // 2)) - 1
            elif array[middle] > target:
                left, right = left, middle
                middle = (-(-(right - left + 1) // 2)) - 1
            print(left, middle,right)
        if target <= l[left]:
            return left
        elif target > l[right]:
            return right+1
        elif l[left] < target <= l[right]:
            return right

# test cases
l=[1,2,4,5,9,11]
print(find_position_bi(l, 10))