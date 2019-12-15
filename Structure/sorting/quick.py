
import random
def quick_sort(array): # TODO
    # def swap(array, i, j):
    #     array[i], array[j]=array[j], array[i]

    def sorting(array, pivot_i):
        left, right = pivot_i, 0
        counter = 0
        for i in range(0, len(array)):
            if array[i] <= array[pivot_i]:
                left = i
            else:
                right = i

            if left > right and array[left]<array[right]:
                array[left], array[right]=array[right], array[left]
                left, right = right, left
                counter += 1
        return counter
    counter = 1
    i=1
    while counter > 0:
        pivot_i = random.choice([0,1,2,3,4])
        counter = sorting(array, pivot_i)
        i += 1
    return array


if __name__ == '__main__':
    print(quick_sort([37, 2, 901, 5, 10,11]))