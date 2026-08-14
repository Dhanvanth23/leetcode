class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count={}
        l=0
        maxx_len=1
        for r in range(len(fruits)):
            count[fruits[r]]=count.get(fruits[r],0)+1
            while len(count)>2:
                count[fruits[l]]-=1
                if count[fruits[l]]==0:
                    del count[fruits[l]]
                l+=1
            maxx_len=max(maxx_len,r-l+1)
        return maxx_len