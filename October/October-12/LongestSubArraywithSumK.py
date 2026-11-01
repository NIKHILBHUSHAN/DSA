class Solution:
    def longestSubarray(self, arr, k):
        s=0
        maxlen=0
        d={}
        for i in range(len(arr)):
            s+=arr[i]
            if s==k:
                maxlen=i+1
            if s-k in d:
                length=i-d[s-k]
                if length>maxlen:
                    maxlen=length
            if s not in d:
                d[s]=i
        return maxlen