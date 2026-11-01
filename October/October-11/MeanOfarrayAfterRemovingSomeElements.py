class Solution(object):
    def trimMean(self, arr):
        nums=[]
        for i in range(len(arr)):
            nums.append(arr[i])
        k=len(nums)//20
        for i in range(k):
            mini=0
            for j in range(1,len(nums)):
                if nums[j]<nums[mini]:
                    mini=j
            nums.pop(mini)

        for i in range(k):
            maxi=0
            for j in range(1,len(nums)):
                if nums[j]>nums[maxi]:
                    maxi=j
            nums.pop(maxi)

        total=0
        for i in range(len(nums)):
            total+=nums[i]

        return total/len(nums)