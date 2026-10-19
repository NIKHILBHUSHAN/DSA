class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """for i in range(len(nums)):
            if nums[i]==0:
                for j in range(i,len(nums)-1):
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
        """
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        while j<len(nums):
            nums[j]=0
            j+=1