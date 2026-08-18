class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        maximum = len(window)
        for ch in s:
            if ch in window:
                index = window.index(ch)
                window += ch
                window = window[index+1 :]
                maximum = max(maximum,len(window))
                
            else:
                window += ch
                maximum = max(maximum,len(window))
        return maximum
        