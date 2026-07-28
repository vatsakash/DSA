class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
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
        if len(s_freq) == len(t_freq):
            for i in s_freq:
                if i in t_freq:
                    if s_freq[i] != t_freq[i]:
                        return False
                else:
                    return False
            return True
        else:
            return False
        