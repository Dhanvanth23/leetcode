class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num]=seen.get(0,num)+1
        return False