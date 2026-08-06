class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_sum = sum(cardPoints[:k])
        maximum = window_sum
        if n > k:
            for i in range(1,k+1):
                window_sum += cardPoints[-i]
                window_sum -= cardPoints[k-i]
                maximum = max(maximum,window_sum)

        return maximum