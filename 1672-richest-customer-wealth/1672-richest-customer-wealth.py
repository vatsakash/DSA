class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        sum = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
            maximum = max(maximum,sum)
            sum = 0
        return maximum
