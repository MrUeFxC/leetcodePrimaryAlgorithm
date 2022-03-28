class Solution:
    def hammingWeight(self, n: int) -> int:
        # # method 1: python & 运算, 都为1时，返回都为1的位数
        # ret = 0
        # for i in range(32):
        #     if n & (1 << i):
        #         ret += 1
        # return ret

        # method 2: 每次与自己减1的数运算，都会把最后一位位1的数变成零
        ret = 0
        while n:
            n &= n - 1
            ret += 1
        return ret



n = 0o0000000000000000000000000001011
s = Solution()
result = s.hammingWeight(n)
print(result)
