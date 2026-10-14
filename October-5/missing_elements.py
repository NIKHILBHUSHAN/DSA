class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """for i in range(len(nums)+1):
            if i not in nums:
                return i"""
        """result=0
        for i in range(len(nums)+1):
            result^=i
        for num in nums:
            result^=num
        return result"""
        sum1=(len(nums)*(len(nums)+1))/2
        sum2=0
        for i in nums:
            sum2+=i
        return int(sum1-sum2)
        