class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            nums[i] = add
        return nums
        