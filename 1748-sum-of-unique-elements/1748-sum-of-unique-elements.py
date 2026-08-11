class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique={}
        sum=0
        for i in nums:
            unique[i]=unique.get(i,0)+1
        for j in unique:
            if unique[j]==1:
                sum+=j
        return sum