class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars=[]
        for ch in s:
            chars.append(ch)
        for i in range(0,len(chars),2*k):
            left=i
            right=min(i+k-1,len(chars)-1)
            while left<right:
                chars[left],chars[right]=chars[right],chars[left]
                left+=1
                right-=1
        result=""
        for ch in chars:
            result+=ch
        return result
            