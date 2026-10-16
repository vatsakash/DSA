class Solution(object):
    def maxProduct(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(arr)
        currmax = arr[0]
        currmin = arr[0]
        max_product = arr[0]
        for i in range(1,n):
            temp = max(arr[i],arr[i]*currmax,arr[i]*currmin)
            currmin = min(arr[i],arr[i]*currmax,arr[i]*currmin)
            currmax = temp 
            max_product = max(max_product,currmax)
        return max_product
        