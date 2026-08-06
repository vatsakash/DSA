class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window_size = s[:k]
        noOfVowels = 0
        for ch in window_size:
            if ch in "aeiou":
                noOfVowels += 1
        maximum = noOfVowels
        for i in range(k,len(s)):
            if s[i] in "aeiou":
                noOfVowels += 1
            if s[i-k] in "aeiou":
                noOfVowels -= 1
            maximum = max(maximum,noOfVowels)
            
        return maximum
        