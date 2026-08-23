class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        freq = {}
        window = []
        max_freq = 0
        maximum = len(window)
        for i in nums:
            if i in freq:
                freq[i] += 1
                if i == 1:
                    max_freq = max(max_freq,freq[i])
            else:
                freq[i] = 1
                if i == 1:
                    max_freq = max(max_freq,freq[i])
            window.append(i)
            if len(window) - max_freq > k:
                freq[window[0]] -= 1
                window = window[1:]
            else:
                maximum = max(maximum,len(window))
        return maximum