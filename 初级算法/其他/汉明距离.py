class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        ret = 0
        while n:
            n &= n-1
            ret += 1
        return ret



x = 1
y = 3
s = Solution()
result = s.hammingDistance(x,y)
print(result)