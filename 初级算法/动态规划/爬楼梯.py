class Solution(object):
    count = 0

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Method 1 递归
        # if n <= 1:
        #     return 1
        # if n < 3:
        #     return n
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # Method 2 + FIbonacci 尾递归
        # return self.Fibonacci(n, 1, 1)

        # Method 3 非递归、
        # if n <= 1:
        #     return 1
        # dp = []
        # dp.append(1)
        # dp.append(2)
        # for i in range(2,n):
        #     dp.append(dp[i-1] + dp[i-2])
        # return dp[n-1]

        # Method 3 非递归优化
        if n <= 2:
            return n
        first, second, sum = 1, 2, 0
        for i in range(n-2):
            sum = first + second
            first = second
            second = sum
        return second

    # Method 2
    # def Fibonacci(self, n, a, b):
    #     if n <= 1:
    #         return b
    #     return self.Fibonacci(n - 1, b, a + b)


n = 4
s = Solution()
result = s.climbStairs(n)
print(result)
