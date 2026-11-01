# Day 19 - Problem 3: Kth Largest Element in an Array
# No sorting libraries, heapq, or built-in sorting shortcuts.

class Solution:
    # Brute Force: Repeatedly find and remove the maximum
    def bruteForce(self, nums, k):
        for i in range(k-1):
            max_index=0

            for j in range(1,len(nums)):
                if nums[j]>nums[max_index]:
                    max_index=j

            nums.pop(max_index)

        max_index=0

        for j in range(1,len(nums)):
            if nums[j]>nums[max_index]:
                max_index=j

        return nums[max_index]

    # Optimal: Quickselect using Lomuto partition
    def findKthLargest(self, nums, k):
        target=len(nums)-k

        def partition(low,high):
            pivot=nums[high]
            i=low-1

            for j in range(low,high):
                if nums[j]<=pivot:
                    i+=1
                    nums[i],nums[j]=nums[j],nums[i]

            nums[i+1],nums[high]=nums[high],nums[i+1]
            return i+1

        low=0
        high=len(nums)-1

        while low<=high:
            p=partition(low,high)

            if p==target:
                return nums[p]
            elif p<target:
                low=p+1
            else:
                high=p-1


if __name__=="__main__":
    nums=[3,2,1,5,6,4]
    k=2

    print("Repeated Maximum:",Solution().bruteForce(nums.copy(),k))
    print("Quickselect:",Solution().findKthLargest(nums.copy(),k))
