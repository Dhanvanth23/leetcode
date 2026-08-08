class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n=len(arr)
        windowsum=sum(arr[:k])
        windowavg=windowsum/k
        count=0
        if windowavg>=threshold:
            count+=1
        for i in range(k,n):
            windowsum=windowsum-arr[i-k]+arr[i]
            windowavg=windowsum/k
            if windowavg>=threshold:
                count+=1
        return count