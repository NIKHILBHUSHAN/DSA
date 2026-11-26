class Solution:
    def countLetters(self,s):
        '''
        count=0
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                valid=True
                for k in range(i+1,j+1):
                    if s[k]!=s[i]:
                        valid=False
                        break
                if valid:
                    count+=1
        return count
        '''
        count=0
        n=len(s)
        i=0
        while i<n:
            j=i
            while j<n and s[j]==s[i]:
                j+=1
            length=j-i
            count+=length*(length+1)//2
            i=j
        return count