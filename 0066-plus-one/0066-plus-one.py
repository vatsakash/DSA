class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i in range(len(digits)):
            number = (10 * number) + digits[i]
        plusone = str(number + 1)
        digits = []
        for i in plusone:
            digits.append(int(i))

        return digits
        