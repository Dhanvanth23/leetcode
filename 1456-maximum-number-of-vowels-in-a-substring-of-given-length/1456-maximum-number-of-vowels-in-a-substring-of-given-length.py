class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        vowels=['a','e','i','o','u']
        wv=s[:k]
        count=0
        for ch in wv:
            if ch in vowels:
                count+=1
        max_count=count
        for i in range(k,n):
            if s[i-k] in vowels:
                count-=1
            if s[i] in vowels:
                count+=1

            max_count=max(max_count,count)
        return max_count