class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        sumOdd = 0
        sumEven = 0
        for i in range(n):
            sumOdd = sumOdd + a
            a += 2
        for i in range(n):
            sumEven = sumEven + b
            b += 2
            
        
        while sumEven != 0:
            sumOdd,sumEven = sumEven,sumOdd % sumEven

        return sumOdd



         

