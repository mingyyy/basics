# 1 to n-1, one duplicate number only


def find_duplicate(l):
    # method1: dictionary
    d = {}
    for i in l:
        if i in d:
            return i
        else:
            d[i] = 0
    # method2: math, since it's 1 to n continuously
    n = len(l)
    sum_1n = (n+1)*n/2
    sum_l = sum(l)
    return sum_l - sum_1n

if __name__=='__main__':
    l = [1,3,4,2,5,2]
    print(find_duplicate(l))