class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1,len(s)):
            first_dig = ord(s[i-1]) - ord('0')
            adj_dig = ord(s[i]) - ord('0')
            dif = abs(adj_dig - first_dig)
            if dif > 2:
                break
            if i == len(s)-1:
                if dif <= 2:
                    return True
        return False