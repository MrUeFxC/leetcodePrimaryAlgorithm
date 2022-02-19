class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        flag = 1
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        if x < 0:
            flag = -1
            x *= -1
        while x > 0:
            num *= 10
            num += (x % 10)
            x = x // 10
        if flag == -1:
            num *= -1
        if num > INT_MAX or num < INT_MIN:
            return 0
        return num

x = 1534236469
s = Solution()
result = s.reverse(x)
print(result)
