class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        p=[0]
        for x in nums:
            p.append(p[-1]+x)
        return p[1:]
