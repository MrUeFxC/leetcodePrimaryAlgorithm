class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res <<= 1
            res += n & 1
            n >>= 1
        return res

n = 0b00000010100101000001111010011100
print(n)
s = Solution()
result = s.reverseBits(n)
print(bin(result))