class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=0
        res1=0
        ls=[]
        rs=[]
        result=[]
        for i in range(len(nums)):
            ls.append(res)
            res+=nums[i]
            rs.append(res1)
            res1+=nums[len(nums)-i-1]
            rs.sort(reverse="True")
        for j in range(len(nums)):
            res=ls[j]-rs[j]
            result.append(abs(res))
        return result
            