class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """squared=[]
        for num in nums:
            squared.append(num*num)
        for i in range(len(squared)):
            for j in range(i+1,len(squared)):
                if squared[i]>squared[j]:
                    temp=squared[i]
                    squared[i]=squared[j]
                    squared[j]=temp
        return squared
        """
        i=0
        j=len(nums)-1
        k=len(nums)-1
        result=[0]*len(nums)
        while i<=j:
            if nums[i]*nums[i]>nums[j]*nums[j]:
                result[k]=nums[i]*nums[i]
                i+=1
            else:
                result[k]=nums[j]*nums[j]
                j-=1
            k-=1
        return result

        