class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        memo = {}

        def solve(i, j):
            if i == j:
                return nums[i]

            if (i, j) in memo:
                return memo[(i, j)]

            left = nums[i] - solve(i + 1, j)
            right = nums[j] - solve(i, j - 1)

            memo[(i, j)] = max(left, right)
            return memo[(i, j)]

        return solve(0, n - 1) >= 0
        