class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        ans = 0
        left,right = 1,x//2
        while left <= right:
            mid = left + (right-left)//2
            sqr = mid*mid
            if sqr == x:
                return mid
            elif sqr < x:
                ans = mid
                left = mid+1
            else:
                right = mid - 1
        return ans