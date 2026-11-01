class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """seen={}
        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        for num in nums:
            if seen[num]>(len(nums)/2):
                return num
        return -1"""
        candidate=None
        count=0
        for num in nums:
            if count==0:
                candidate=num
            if candidate==num:
                count+=1
            else:
                count-=1
        return candidate
        