class Solution:
    def longestNiceSubstring(self,s):
        '''
        n=len(s)
        longest=""
        for i in range(n):
            for j in range(i,n):
                sub=s[i:j+1]
                nice=True
                for ch in sub:
                    if ch.islower():
                        if ch.upper() not in sub:
                            nice=False
                            break
                    else:
                        if ch.lower() not in sub:
                            nice=False
                            break
                if nice and len(sub)>len(longest):
                    longest=sub
        return longest
        '''
        def solve(s):
            if len(s)<2:
                return ""
            chars=set(s)
            for i in range(len(s)):
                ch=s[i]
                if ch.lower() not in chars or ch.upper() not in chars:
                    left=solve(s[:i])
                    right=solve(s[i+1:])
                    if len(left)>=len(right):
                        return left
                    return right
            return s
        return solve(s)