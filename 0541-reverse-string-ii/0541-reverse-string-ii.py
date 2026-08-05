class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        chars = list(s)
        n = len(chars)
        for i in range(0,n,k*2):
            left = i
            right = min(i + k -1,n-1)
            while left < right:
                chars[left],chars[right] = chars[right],chars[left]
                left += 1
                right -= 1
        return "".join(chars)