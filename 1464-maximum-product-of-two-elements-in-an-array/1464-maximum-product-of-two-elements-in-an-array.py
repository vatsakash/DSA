class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        i = 0
        j = 1
        product = (nums[i]-1) * (nums[j]-1)
        return product