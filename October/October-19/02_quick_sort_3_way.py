# Day 19 - Problem 2: Quick Sort with 3-Way Partition
# No sorting libraries or built-in sorting shortcuts.

class Solution:
    # Brute Force: Selection Sort
    def bruteForce(self, nums):
        n=len(nums)

        for i in range(n):
            min_index=i

            for j in range(i+1,n):
                if nums[j]<nums[min_index]:
                    min_index=j

            nums[i],nums[min_index]=nums[min_index],nums[i]

        return nums

    # Optimal: 3-Way Quick Sort (Dutch National Flag partition)
    def sortArray(self, nums):
        def quick_sort(low,high):
            if low>=high:
                return

            pivot=nums[(low+high)//2]
            lt=low
            mid=low
            gt=high

            while mid<=gt:
                if nums[mid]<pivot:
                    nums[lt],nums[mid]=nums[mid],nums[lt]
                    lt+=1
                    mid+=1
                elif nums[mid]>pivot:
                    nums[mid],nums[gt]=nums[gt],nums[mid]
                    gt-=1
                else:
                    mid+=1

            quick_sort(low,lt-1)
            quick_sort(gt+1,high)

        quick_sort(0,len(nums)-1)
        return nums


if __name__=="__main__":
    nums=[4,2,4,1,4,3,2,4]
    print("Selection Sort:",Solution().bruteForce(nums.copy()))
    print("3-Way Quick Sort:",Solution().sortArray(nums.copy()))
