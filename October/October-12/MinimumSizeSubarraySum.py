class Solution:
    def minSubArrayLen(self,target:int,nums:list[int])->int:
        """minlen=len(nums)+1
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                if s>=target:
                    length=j-i+1
                    if length<minlen:
                        minlen=length
        if minlen==len(nums)+1:
            return 0
        return minlen"""
        left=0
        current_sum=0
        min_length=float('inf')
        for right in range(len(nums)):
            current_sum+=nums[right]
            while current_sum>=target:
                length=right-left+1
                if length<min_length:
                    min_length=length
                current_sum-=nums[left]
                left+=1
        if min_length==float('inf'):
            return 0
        return min_length