class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum=[]
        for i in range(len(nums)):
            if i==0:
                sum.append(nums[i])
            else:
                sum.append(sum[i-1]+nums[i])
        return sum