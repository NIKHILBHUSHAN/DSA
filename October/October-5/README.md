1.Intersection of Two Arrays

Find the unique elements of nums1 and traverse the nums2 if the element in nums2 present in nums1 unique elements add them to result set 

Time Complexity : O(n+m)

where n is length of nums1 and m is length of nums2 building the set from nums1 is O(n) then scanning nums2 and checking membership is O(m)

2.Missing elements:

XOR Approach:

start result with 0 and perform XOR on every number from 0 to n and XOR every number on the elements of num so duplicates values cancel leaving the missing value

Sum of n elements Approach:

calculate the sum of n numbers using teh formula n(n+1)/2 and calculate the sumo all elements in the array and subtarct these two sums gives the missing number

Time Complexity : O(n)

3.Find all missing elements:

Set Approach:

find the unique elements in the array and the traverse from 1 to n if the anynumber is not present in unique elements append it to result and return the result

Boolean Approach:

create an boolean list with false as default value of sixe (n+1) and traverse the array and mark true at the position of the num and traverse from 1 to n if any element in boolean list is false append it to result and return the result

Time Complexity; O(n)