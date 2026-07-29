class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        ans = []
        for num in freq:
            if freq[num] > n // 3:
                ans.append(num)

        return ans