1.runningsum.py:

using the loop calculate the sum of the elements.

Time complexity : O(n)

2.pivot index:

calculate the total sum once calculate the right sum using the formula rightsum=totalsum-leftsum-currentelement compare both sums and then update the left sum.

Time complexity : O(n)

3.RangesumQuery :

calcualte the prefix sum array and find the range sum by the formula array[right]- array[left-1] and return the result.

Time complexity : O(n)