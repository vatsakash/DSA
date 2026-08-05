class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected = (n*(n+1))//2
        actual_sum = 0
        for i in range(n):
            actual_sum += nums[i]

        return expected - actual_sum


        