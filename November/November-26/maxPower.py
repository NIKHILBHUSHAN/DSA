class Solution:
    def maxPower(self,s):
        '''
        best=0
        n=len(s)
        for i in range(n):
            count=1
            j=i+1
            while j<n and s[j]==s[i]:
                count+=1
                j+=1
            if count>best:
                best=count
        return best
        '''
        best=1
        current=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                current+=1
            else:
                current=1
            if current>best:
                best=current
        return best