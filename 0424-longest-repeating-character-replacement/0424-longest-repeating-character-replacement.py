class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        window = []
        maximum = len(window)
        max_freq = 0
        for ch in s:
            if ch in freq:
                freq[ch] += 1
                max_freq = max(max_freq,freq[ch])
            else:
                freq[ch] = 1
                max_freq = max(max_freq,freq[ch])
            window.append(ch)
            if len(window) - max_freq > k:
                freq[window[0]] -= 1
                window = window[1:]
            else:
                maximum = max(maximum,len(window))
        
        return maximum
