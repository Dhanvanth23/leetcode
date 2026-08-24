class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        result = []

        for x in nums:
            right = total - left - x
            result.append(abs(left - right))
            left += x

        return result