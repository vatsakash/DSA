class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first_word = strs[0]
        matched_strs = ""
        i = 1
        j = 0 
        if len(strs) > 1:
            while j < len(strs[i]) and j < len(first_word) :
                if first_word[j] == strs[i][j]:
                    if i == len(strs)-1:
                        matched_strs += first_word[j]
                        i = 1
                        j += 1
                    else:
                        i += 1
                else:
                    break
            return matched_strs
        else:
            return strs[0]