class Solution:
    def toHex(self,num):
        '''
        if num==0:
            return "0"
        digits="0123456789abcdef"
        if num<0:
            num=num+2**32
        res=""
        while num>0:
            rem=num%16
            res=digits[rem]+res
            num=num//16
        return res
        '''
        if num==0:
            return "0"
        digits="0123456789abcdef"
        num=num&0xffffffff
        res=""
        while num>0:
            rem=num&15
            res=digits[rem]+res
            num=num>>4
        return res