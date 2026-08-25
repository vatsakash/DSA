class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = 1
        i = k
        while i in nums:
            i = n*k
            n += 1
        return i


        