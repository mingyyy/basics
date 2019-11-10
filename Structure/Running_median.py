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
        if n_left>n_right:
            node = -heapq.heappop(left)
            heapq.heappush(right, node)
        else:
            node = heapq.heappop(right)
            heapq.heappush(left, -node)
    if nums==[]:
        return None
    elif len(nums) == 1:
        return nums[0]
    left = heapq.heapify([])
    right = heapq.heapify([])
    i, n_left, n_right = 0, 0, 0
    # construct heaps: maxHeap = left, minHeap = right
    while i < len(nums):
        if left is None or -left[0] < nums[i]:
            heapq.heappush(left, -nums[i])
            n_left += 1
        if right is None or right[0] < nums[i]:
            heapq.heappush(right, nums[i])
            n_right += 1
        if abs(n_left - n_right) >= 2:
            balance(left, right)
        i += 1

    # get median
    if len(nums)%2 == 0:
        median = (left[0] + right[0])/2
    else:
        if n_left>n_right:
            median = left[0]
        else:
            median = right[0]
    return median


if __name__=='__main__':
    print(running_median([2, 5, 7, 10, 1, 0, 8]))




