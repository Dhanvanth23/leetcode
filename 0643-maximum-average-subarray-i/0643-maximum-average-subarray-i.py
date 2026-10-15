class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        summ=sum(nums[:k])
        maxx_sum=summ
        for i in range(k,n):
            summ=summ-nums[i-k]+nums[i]
            maxx_sum=max(maxx_sum,summ)
        return maxx_sum/k