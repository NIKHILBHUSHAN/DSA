# Day 19 - Problem 1: Quick Sort
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

    # Optimal: Quick Sort using Lomuto Partition
    def quickSortLomuto(self, nums):
        def partition(low,high):
            pivot=nums[high]
            i=low-1

            for j in range(low,high):
                if nums[j]<=pivot:
                    i+=1
                    nums[i],nums[j]=nums[j],nums[i]

            nums[i+1],nums[high]=nums[high],nums[i+1]
            return i+1

        def quick_sort(low,high):
            if low<high:
                p=partition(low,high)
                quick_sort(low,p-1)
                quick_sort(p+1,high)

        quick_sort(0,len(nums)-1)
        return nums

    # Optimal: Quick Sort using Hoare Partition
    def quickSortHoare(self, nums):
        def partition(low,high):
            pivot=nums[(low+high)//2]
            i=low-1
            j=high+1

            while True:
                i+=1
                while nums[i]<pivot:
                    i+=1

                j-=1
                while nums[j]>pivot:
                    j-=1

                if i>=j:
                    return j

                nums[i],nums[j]=nums[j],nums[i]

        def quick_sort(low,high):
            if low<high:
                p=partition(low,high)
                quick_sort(low,p)
                quick_sort(p+1,high)

        quick_sort(0,len(nums)-1)
        return nums


if __name__=="__main__":
    nums=[10,7,8,9,1,5]

    print("Selection Sort:",Solution().bruteForce(nums.copy()))
    print("Lomuto Quick Sort:",Solution().quickSortLomuto(nums.copy()))
    print("Hoare Quick Sort:",Solution().quickSortHoare(nums.copy()))
