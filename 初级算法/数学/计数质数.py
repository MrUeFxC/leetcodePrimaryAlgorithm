import math


class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [1]*n
        ans = 0
        for i in range(2,n):
            if isPrime[i] == 1:
                ans += 1
                for j in range(i*i, n, i):
                    isPrime[j] = 0
        return ans


n = 15
s = Solution()
result = s.countPrimes(n)
print(result)