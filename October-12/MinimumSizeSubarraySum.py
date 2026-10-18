class Solution(object):
    def minSubArrayLen(self, target, nums):
        s=0
        minlen=len(nums)+1
        left=0
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target:
                if i-left+1<minlen:
                    minlen=i-left+1
                s-=nums[left]
                left+=1
        if minlen==len(nums)+1:
            return 0
        return minlen