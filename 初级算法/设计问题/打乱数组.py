import random


class Solution(object):
    def __init__(self, nums):
        self.nums = nums
        self.original = nums.copy()

    def reset(self):
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self):
        shuffled = [0] * len(self.nums)
        for i in range(len(self.nums)):
            j = random.randrange(len(self.nums))
            shuffled[i] = self.nums.pop(j)
        self.nums = shuffled
        return self.nums




nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)