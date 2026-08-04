class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        smallest = nums[0]
        largest = nums[-1]
        a = 0
        missing = []
        for i in range(smallest,largest + 1):
            if nums[a] != i:
                missing.append(i)
            else:
                a += 1
        return missing
        