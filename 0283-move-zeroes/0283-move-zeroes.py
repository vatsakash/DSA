class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        b = 0
        for a in range(len(nums)):
            if nums[a] != 0:
                temp = nums[b]
                nums[b] = nums[a]
                nums[a] = temp
                b += 1

        return nums
        