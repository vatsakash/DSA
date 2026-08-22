class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0
        product = 1
        original_number = n
        while n > 0:
            digit = n % 10
            sum += digit
            product *= digit
            n = n // 10

        if original_number % (sum + product) == 0:
            return True
        else:
            return False
        