class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lowerstr = ""
        start = 0
        for char in s :
            if char.isalnum():
                lowerstr += char.lower()

        end = len(lowerstr)-1
        while start < end:
            if lowerstr[start] == lowerstr[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
