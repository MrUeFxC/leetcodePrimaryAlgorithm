from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        first, second = nums[0], float('inf')
        for i in range(1, n):
            num = nums[i]
            if num > second:
                return True
            if num > first:
                second = num
            else:
                first = num
        return False


nums = [5,4,3,2,1,2,3]
s = Solution()
result = s.increasingTriplet(nums)
print(result)

