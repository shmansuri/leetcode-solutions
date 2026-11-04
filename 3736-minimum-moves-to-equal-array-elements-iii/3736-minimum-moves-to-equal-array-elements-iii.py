class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        bada = max(nums)

        for i in range(len(nums)):
            if nums[i] < bada:
                diff= bada - nums[i]
                count += diff
        
        return count
        