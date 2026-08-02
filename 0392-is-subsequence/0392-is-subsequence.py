class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = 0
        b = 0
        if len(s) > 0:
            while b < len(t):
                if t[b] == s[a]:
                    if a == len(s)-1:
                        return True
                    a += 1
                    b += 1
                else:
                    b += 1
            return False
        else:
            return True
            
             
            

        return True
        