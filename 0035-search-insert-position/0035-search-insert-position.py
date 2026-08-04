class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i 
            if i != len(nums)-1:
                if nums[i] < target < nums[i+1]:
                    return i+1
                elif target < nums[i]:
                    return i
            else:
                if target > nums[i]:
                    return i+1
                elif target < nums[i]:
                    return i 
