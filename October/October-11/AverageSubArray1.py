class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """maxsum=float('-inf')
        for i in range(len(nums)-k+1):
            total=0
            for j in range(i,i+k):
                total+=nums[j]
            if total>maxsum:
                maxsum=total
        return maxsum/k"""


        sum=0
        for i in range(k):
            sum+=nums[i]
        maxsum=sum
        for i in range(k,len(nums)):
            sum+=nums[i]-nums[i-k]
            if sum>maxsum:
                maxsum=sum
        return maxsum/k
        