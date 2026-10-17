class Solution(object):
    def findMaxAverage(self, nums, k):
        s=0
        for i in range(k):
            s+=nums[i]
        maxsum=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            if s>maxsum:
                maxsum=s
        return maxsum/k