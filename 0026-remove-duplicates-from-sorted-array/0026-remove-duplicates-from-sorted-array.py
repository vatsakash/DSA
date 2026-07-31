class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        k = 1
        for i in range(1,len(nums)):
            if nums[a] != nums[i]:
                a += 1
                nums[a] = nums[i]
                k += 1

        return k
        