class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        left = 0
        max = 0
        for i in range(1, len(prices)):
            base = prices[left]
            # 这一步计算比当前基准更小的的数
            diff = prices[i] - base
            if diff < 0:
                left = i
                continue
            if diff > max:
                max = diff
        return max

prices = [7,1,5,3,6,4]
s = Solution()
result = s.maxProfit(prices)
print(result)