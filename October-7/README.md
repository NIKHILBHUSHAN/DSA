1.Rotate Array:

use two pointers left=0 and right=n-1 where n is the length of the array and swap the left and right indexes and increment left and decrement right until left<right

Time Complexity:O(n)

2.Rotate array by K steps:

Reverse the entire array and then reverse the first K elements and then reverse the remaining elements 

Time Complexity:O(n)

3.Rotate array by groups:

set left as teh groups starting index and right=left+k-1 and len(arr)-1 and swap the elements moving inwards and move to the next group by adding k to the starting index

Time Complexity : O(n)