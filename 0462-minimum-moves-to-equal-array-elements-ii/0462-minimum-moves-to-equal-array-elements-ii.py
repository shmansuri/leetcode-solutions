class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        #sort the list
        nums.sort()
        #find the middle index values 
        #we can write n= len(nums)//2 => diff = nums[n]
        diff = nums[len(nums)//2]
        result = 0
        
        for i in nums:
            result += abs(diff - i)
        return result

                

        