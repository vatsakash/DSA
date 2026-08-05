class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        window_avg = window_sum / k
        maximum = window_avg
        for i in range(k,len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]
            window_avg = window_sum / k
            maximum = max(maximum,window_avg)

        return maximum