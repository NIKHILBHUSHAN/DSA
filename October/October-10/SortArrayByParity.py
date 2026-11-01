class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """result=[0]*len(nums)
        i=0
        for num in nums:
            if num%2==0:
                result[i]=num
                i+=1
        for num in nums:
            if num%2!=0:
                result[i]=num
                i+=1
        return result"""
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]%2==0:
                i+=1
            elif nums[j]%2!=0:
                j-=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        return nums
                
