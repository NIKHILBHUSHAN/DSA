class Solution:
    def maxSubarraySum(self,arr,k):
        """max_sum=float('-inf')
        for i in range(len(arr)-k+1):
            current_sum=0
            for j in range(i,i+k):
                current_sum+=arr[j]
            max_sum=max(max_sum,current_sum)
        return max_sum"""
        window_sum=0
        for i in range(k):
            window_sum+=arr[i]
        max_sum=window_sum
        for i in range(k,len(arr)):
            window_sum=window_sum+arr[i]-arr[i-k]
            if window_sum>max_sum:
                max_sum=window_sum
        return max_sum