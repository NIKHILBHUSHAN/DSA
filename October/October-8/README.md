1. valid Palindrome:

Use two pointer technique where left=0 and right=len(string)-1 and if at any point if left and right characters are not equal return False if it succesfully completes teh string then return True

Time Complexity:O(n)

2. Reverse String:

Use two pointer left=0 and right=len(string)-1 and swap the left and right elements using a temp variabel until left<right

Time complexity:O(n)

3.Reverse Vowels:

convert the string into list of characters Use two pointer technique where left=0 and right=len(string)-1 and use two separate loops to find out teh vowels and whenever they are finded then swap them and return the list converted into string
