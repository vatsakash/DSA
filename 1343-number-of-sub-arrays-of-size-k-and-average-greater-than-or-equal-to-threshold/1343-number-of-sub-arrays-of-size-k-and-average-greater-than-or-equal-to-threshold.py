class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        window_avg = window_sum / k
        noOfSubarray = 0
        if window_avg >= threshold:
            noOfSubarray += 1
        for i in range(k,len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i-k]
            window_avg = window_sum / k
            if window_avg >= threshold:
                noOfSubarray += 1
        return noOfSubarray

        