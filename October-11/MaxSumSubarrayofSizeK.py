class Solution:
    def maxSubarraySum(self, arr, k):
        s=0
        for i in range(k):
            s+=arr[i]
        maxsum=s
        for i in range(k,len(arr)):
            s+=arr[i]-arr[i-k]
            if s>maxsum:
                maxsum=s
        return maxsum