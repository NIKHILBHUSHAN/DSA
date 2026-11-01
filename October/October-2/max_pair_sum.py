class Solution:
    def maxSum(self, nums: list[int]) -> int:
        largest={}
        result=-1
        for num in nums:          
            temp=num
            maxdigit=0
            while temp>0:
                digit=temp%10
                if digit>maxdigit:
                    maxdigit=digit
                temp//=10
            if maxdigit in largest:
                pairsum=largest[maxdigit]+num
                if pairsum>result:
                    result=pairsum
                if num>largest[maxdigit]:
                    largest[maxdigit] = num
            else:
                largest[maxdigit] = num
        return result
