class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ins=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[ins]=nums[ins],nums[i]
                ins+=1