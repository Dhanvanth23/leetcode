class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        res = {}
        maxx_len = 0

        for r in range(len(nums)):
            res[nums[r]] = res.get(nums[r], 0) + 1

            while res[nums[r]] > k:
                res[nums[l]] -= 1
                l += 1

            maxx_len = max(maxx_len, r - l + 1)

        return maxx_len