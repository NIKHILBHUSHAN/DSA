class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        unique=set(nums)
        result=[]
        for num in range(1,len(nums)+1):
            if num not in unique:
                result.append(num)
        return result
        """n=len(nums)
        present=[False]*(n+1)
        for num in nums:
            present[num]=True
        result=[]
        for num in range(1,n+1):
            if not present[num]:
                result.append(num)
        return result"""
        