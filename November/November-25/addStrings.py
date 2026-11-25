class Solution:
    def addStrings(self,num1,num2):
        '''
        a=int(num1)
        b=int(num2)
        return str(a+b)
        '''
        i=len(num1)-1
        j=len(num2)-1
        carry=0
        res=""
        while i>=0 or j>=0 or carry>0:
            total=carry
            if i>=0:
                total+=ord(num1[i])-ord('0')
                i-=1
            if j>=0:
                total+=ord(num2[j])-ord('0')
                j-=1
            res=chr(total%10+ord('0'))+res
            carry=total//10
        if res=="":
            return "0"
        return res