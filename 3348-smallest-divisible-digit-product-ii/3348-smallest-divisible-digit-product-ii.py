class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp_t = t
        req_a = req_b = req_c = req_d = 0
        
        # Factorize t into powers of 2, 3, 5, and 7
        while temp_t % 2 == 0:
            req_a += 1
            temp_t //= 2
        while temp_t % 3 == 0:
            req_b += 1
            temp_t //= 3
        while temp_t % 5 == 0:
            req_c += 1
            temp_t //= 5
        while temp_t % 7 == 0:
            req_d += 1
            temp_t //= 7
            
        # If t has any prime factor > 7, it's impossible using digits 1-9
        if temp_t > 1:
            return "-1"

        # Precompute DP table: dp[a][b] = min digits needed for 'a' twos and 'b' threes
        INF = float('inf')
        dp = [[INF] * 60 for _ in range(60)]
        dp[0][0] = 0
        
        for i in range(55):
            for j in range(55):
                if dp[i][j] == INF:
                    continue
                # Transitions for digits {2, 3, 4, 6, 8, 9}
                dp[min(55, i + 1)][j] = min(dp[min(55, i + 1)][j], dp[i][j] + 1)             # 2
                dp[i][min(55, j + 1)] = min(dp[i][min(55, j + 1)], dp[i][j] + 1)             # 3
                dp[min(55, i + 2)][j] = min(dp[min(55, i + 2)][j], dp[i][j] + 1)             # 4
                dp[min(55, i + 1)][min(55, j + 1)] = min(dp[min(55, i + 1)][min(55, j + 1)], dp[i][j] + 1) # 6
                dp[min(55, i + 3)][j] = min(dp[min(55, i + 3)][j], dp[i][j] + 1)             # 8
                dp[i][min(55, j + 2)] = min(dp[i][min(55, j + 2)], dp[i][j] + 1)             # 9

        # Propagate backwards to cover >= 'a' twos and >= 'b' threes
        for i in range(54, -1, -1):
            for j in range(54, -1, -1):
                dp[i][j] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1])

        def min_len(a, b, c, d):
            a = max(0, min(55, a))
            b = max(0, min(55, b))
            c = max(0, c)
            d = max(0, d)
            return c + d + dp[a][b]

        def get_factors(digit):
            if digit == 2: return 1, 0, 0, 0
            if digit == 3: return 0, 1, 0, 0
            if digit == 4: return 2, 0, 0, 0
            if digit == 5: return 0, 0, 1, 0
            if digit == 6: return 1, 1, 0, 0
            if digit == 7: return 0, 0, 0, 1
            if digit == 8: return 3, 0, 0, 0
            if digit == 9: return 0, 2, 0, 0
            return 0, 0, 0, 0

        def build_suffix(length, a, b, c, d):
            res = []
            for i in range(length):
                for digit in range(1, 10):
                    da, db, dc, dd = get_factors(digit)
                    if length - 1 - i >= min_len(a - da, b - db, c - dc, d - dd):
                        res.append(str(digit))
                        a -= da
                        b -= db
                        c -= dc
                        d -= dd
                        break
            return "".join(res)

        n = len(num)
        first_zero = num.find('0')

        # Prefix factor tracking
        pref_a = [0] * (n + 1)
        pref_b = [0] * (n + 1)
        pref_c = [0] * (n + 1)
        pref_d = [0] * (n + 1)

        for i in range(n):
            pref_a[i + 1] = pref_a[i]
            pref_b[i + 1] = pref_b[i]
            pref_c[i + 1] = pref_c[i]
            pref_d[i + 1] = pref_d[i]
            if num[i] != '0':
                da, db, dc, dd = get_factors(int(num[i]))
                pref_a[i + 1] += da
                pref_b[i + 1] += db
                pref_c[i + 1] += dc
                pref_d[i + 1] += dd

        # 1. Check if num itself is valid
        if first_zero == -1:
            if (pref_a[n] >= req_a and pref_b[n] >= req_b and 
                pref_c[n] >= req_c and pref_d[n] >= req_d):
                return num

        # 2. Try matching a prefix of length p (from n-1 down to 0)
        for p in range(n - 1, -1, -1):
            if first_zero != -1 and p > first_zero:
                continue

            start_digit = int(num[p]) + 1
            for d in range(start_digit, 10):
                da, db, dc, dd = get_factors(d)

                rem_a = req_a - pref_a[p] - da
                rem_b = req_b - pref_b[p] - db
                rem_c = req_c - pref_c[p] - dc
                rem_d = req_d - pref_d[p] - dd

                rem_len = n - 1 - p
                if rem_len >= min_len(rem_a, rem_b, rem_c, rem_d):
                    prefix = num[:p] + str(d)
                    suffix = build_suffix(rem_len, rem_a, rem_b, rem_c, rem_d)
                    return prefix + suffix

        # 3. Fallback: smallest number of length > N
        target_len = max(n + 1, min_len(req_a, req_b, req_c, req_d))
        return build_suffix(target_len, req_a, req_b, req_c, req_d)