class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u']
        chars=list(s)
        left=0
        right=len(s)-1
        while left<right:
            while left<right and chars[left].lower() not in vowels:
                left+=1
            while left<right and chars[right].lower() not in vowels:
                right-=1
            temp=chars[left]
            chars[left]=chars[right]
            chars[right]=temp
            left+=1
            right-=1
        return "".join(chars)
        