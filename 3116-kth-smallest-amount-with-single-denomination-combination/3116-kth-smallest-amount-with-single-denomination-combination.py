class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        filtered_coins = []
        for c in coins:
            if not any(c % x == 0 for x in filtered_coins):
                filtered_coins.append(c)
        
        n = len(filtered_coins)
        
        # Step 2: Helper function to count unique amounts <= M using Inclusion-Exclusion
        def count_amounts_le(M: int) -> int:
            total_count = 0
            
            # Iterate through all non-empty subsets using bitmasking
            for mask in range(1, 1 << n):
                current_lcm = 1
                bits_set = 0
                
                for i in range(n):
                    if (mask >> i) & 1:
                        bits_set += 1
                        current_lcm = math.lcm(current_lcm, filtered_coins[i])
                        if current_lcm > M:  # Optimization: overflow/exceeding threshold
                            break
                            
                multiples = M // current_lcm
                if bits_set % 2 == 1:
                    total_count += multiples
                else:
                    total_count -= multiples
                    
            return total_count

        # Step 3: Binary Search for the K-th smallest amount
        low = filtered_coins[0]
        high = filtered_coins[0] * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_amounts_le(mid) >= k:
                ans = mid
                high = mid - 1  # Try finding a smaller valid amount
            else:
                low = mid + 1   # Need a larger amount
                
        return ans