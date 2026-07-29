class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        nums = sorted(arr)
        freq = {}
        rank = 0
        ranking = []
        for i in nums:
            if i in freq:
                if rank == 0:
                    rank += 1

                freq[i] = rank
            else:
                rank += 1
                freq[i] = rank

        for i in arr:
            ranking.append(freq[i])

        return ranking

        