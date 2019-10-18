# Leetcode: 189. Rotate Array
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # option1
        if len(nums)>1:
            if len(nums)<=k:
                k= k % len(nums)
            # nums[:] create a copy <> num
            nums[:]=nums[-k:]+nums[:-k]

# coding interview book
#