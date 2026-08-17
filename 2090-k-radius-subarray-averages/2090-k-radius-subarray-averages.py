class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        window_size = 2 * k + 1

        if window_size > n:
            return ans

        window = sum(nums[:window_size])

        ans[k] = window // window_size

        for r in range(window_size, n):
            window = window - nums[r - window_size] + nums[r]

            center = r - k
            ans[center] = window // window_size

        return ans