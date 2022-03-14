class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1 and n % 3 == 0:
            n = n / 3
        return n == 1


n = 6
s = Solution()
result = s.isPowerOfThree(n)
print(result)

