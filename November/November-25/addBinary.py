class Solution:
    def addBinary(self,a,b):
        '''
        x=int(a,2)
        y=int(b,2)
        res=""
        while x>0 or y>0:
            rem=(x%2+y%2)%2
            res=str(rem)+res
            x=x//2
            y=y//2
        return res
        '''
        i=len(a)-1
        j=len(b)-1
        carry=0
        res=""
        while i>=0 or j>=0 or carry>0:
            total=carry
            if i>=0:
                total+=int(a[i])
                i-=1
            if j>=0:
                total+=int(b[j])
                j-=1
            res=str(total%2)+res
            carry=total//2
        if res=="":
            return "0"
        return res