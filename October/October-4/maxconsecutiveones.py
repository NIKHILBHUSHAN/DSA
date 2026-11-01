class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxcount=0
        presentcount=0
        for num in nums:
            if num==1:
                presentcount+=1
                if presentcount>maxcount:
                    maxcount=presentcount
            else:
                
                presentcount=0
        return maxcount
        