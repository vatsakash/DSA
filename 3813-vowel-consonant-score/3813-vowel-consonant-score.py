class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = 0
        c = 0
        for alp in s :
            if alp == 'a' or alp == 'e' or alp == 'i' or alp == 'o' or alp == 'u':
                v += 1
            elif alp == " " or alp.isdigit():
                continue
            else:
                c += 1
        if c>0:
            score = int(floor(v/c))
            return score
        else:
            return 0