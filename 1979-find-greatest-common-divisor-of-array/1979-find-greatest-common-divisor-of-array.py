class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        grtst_num = nums[-1]
        smlst_num = nums[0]
        gcd = 1
        for i in range(1,smlst_num + 1):
            if grtst_num % i == 0 and smlst_num % i == 0:
                gcd = i
        return gcd




        