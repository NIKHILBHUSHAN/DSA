class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """for i in range(len(nums)):
            leftsum=0
            rightsum=0
            for j in range(0,i):
                leftsum+=nums[j]
            for j in range(i+1,len(nums)):
                rightsum+=nums[j]
            if leftsum==rightsum:
                return i
        return -1"""
        leftsum=0
        totalsum=0
        for num in nums:
            totalsum+=num
        for i in range(len(nums)):   
            rightsum=totalsum-leftsum-nums[i]
            if rightsum==leftsum:
                return i
            leftsum+=nums[i]
        return -1