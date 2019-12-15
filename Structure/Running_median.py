'''
Using a min-heap and a max-heap to calculate the running median
Python heapq is min-heap, priority queue
Heaps are binary trees for which every parent node has a value less than or equal to any of its children.
This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k,
counting elements from zero. For the sake of comparison, non-existing elements are considered to be infinite.
The interesting property of a heap is that its smallest element is always the root, heap[0].
'''

import heapq

def running_median(nums):
    def balance(left, right):
        if len(left) > len(right):
            node = -heapq.heappop(left)
            heapq.heappush(right, node)
        else:
            node = heapq.heappop(right)
            heapq.heappush(left, -node)

    def addMedian(num, left, right):
        if left==[] or  nums[i] < -left[0]:
            heapq.heappush(left, -nums[i])
        else:
            heapq.heappush(right, nums[i])

    def getMedian(left, right):
        if len(nums) % 2 == 0:
            median = (-left[0] + right[0]) / 2
        else:
            if len(left) > len(right):
                median = -left[0]
            else:
                median = right[0]
        return median


    if nums == []:
        return None
    elif len(nums) == 1:
        return nums[0]
    # construct heaps: maxHeap = left, minHeap = right
    left = []
    right = []
    i = 0

    while i < len(nums):
        addMedian(nums[i], left, right)
        if abs(len(left) - len(right)) >= 2:
            balance(left, right)
        i += 1
        # print(left, right)
    # get median
    median = getMedian(left, right)

    return median


if __name__=='__main__':
    print(running_median([1, 3, -5, 6, 8, 1]))




