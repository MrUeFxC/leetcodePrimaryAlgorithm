class Solution:
    def missingNumber(self, nums) -> int:
        xor = 0
        for i in range(len(nums)):
            xor ^= nums[i] ^ (i+1)
        return xor

nums = [3, 0, 1]
s = Solution()
result = s.missingNumber(nums)
print(result)