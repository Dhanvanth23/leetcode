class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        need={}
        for c in s1:
            need[c]=need.get(c,0)+1
        window={}
        left=0
        for right in range(len(s2)):
            c=s2[right]
            window[c]=window.get(c,0)+1
            if right-left+1>len(s1):
                leftchar=s2[left]
                window[leftchar] -=1
                if window[leftchar]==0:
                    del window[leftchar]
                left+=1
            if need==window:
                return True
        return False