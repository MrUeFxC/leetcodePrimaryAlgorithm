class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numLength = len(nums)
        if numLength < 1:
            return 0
        elif numLength < 2:
            return nums[0]
        sum = 0
        max = nums[0]
        for i in range(0, len(nums)):
            sum += nums[i]
            if sum < 0:
                sum = 0
                if nums[i] > max:
                    max = nums[i]
            else:
                if sum < nums[i]:
                    max = nums[i]
                    sum = 0
                    continue
                if sum > max:
                    max = sum
        return max

nums = [-2,-3]
s = Solution()
result = s.maxSubArray(nums)
print(result)