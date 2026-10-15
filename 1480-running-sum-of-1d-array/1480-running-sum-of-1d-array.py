class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        p=[0]
        for i in range(len(nums)):
            p.append(p[-1]+nums[i])
        return p[1:]
