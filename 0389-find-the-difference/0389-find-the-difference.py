class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_freq = {}
        t_freq = {}
        for char in s:
            if char in s_freq:
                s_freq[char] += 1
            else:
                s_freq[char] = 1
        for char in t:
            if char in t_freq:
                t_freq[char] += 1
            else:
                t_freq[char] = 1
        for ch in t_freq:
            if ch in s_freq:
                if t_freq[ch] != s_freq[ch]:
                    return ch
                
            else:
                return ch