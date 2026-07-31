class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a,k = 0,0
        for i in range(0,len(nums)):
            if nums[i] == val:
                k += 1
            else:
                nums[a] = nums[i]
                a += 1
            
        
        return len(nums)-k
        