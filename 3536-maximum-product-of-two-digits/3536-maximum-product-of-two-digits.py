class Solution(object):
    def maxProduct(self, n):
        digits = []
        num = 0
        while n > 0:
            num = n%10
            n=n//10
            digits.append(num)
        digits.sort(reverse=True)
        product = digits[0] * digits[1]
        return product