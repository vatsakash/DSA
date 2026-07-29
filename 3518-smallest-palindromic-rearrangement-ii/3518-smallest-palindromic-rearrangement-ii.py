class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        half = [0] * 26
        middle = ""

        m = 0
        for i in range(26):
            half[i] = freq[i] // 2
            m += half[i]
            if freq[i] & 1:
                middle = chr(i + ord('a'))

        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i

        ways = fact[m]
        for x in half:
            ways //= fact[x]

        if ways < k:
            return ""

        ans = []

        rem = m

        while rem:
            for i in range(26):
                if half[i] == 0:
                    continue

                # Number of permutations if we place this character
                newWays = ways * half[i] // rem

                if newWays >= k:
                    ans.append(chr(i + ord('a')))
                    half[i] -= 1
                    ways = newWays
                    rem -= 1
                    break
                else:
                    k -= newWays

        first = "".join(ans)
        return first + middle + first[::-1]