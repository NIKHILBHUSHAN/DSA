class Solution:
    def countAndSay(self, n: int) -> str:
        result="1"
        for i in range(n-1):
            new=""
            count=1
            for j in range(1,len(result)):
                if result[j]==result[j-1]:
                    count+=1
                else:
                    new+=str(count)+result[j-1]
                    count=1
            new+=str(count)+result[-1]
            result=new
        return result
        """result="1"
        for i in range(n-1):
            group=[]
            j=0
            while j<len(result):
                ch=result[j]
                count=0
                while j<len(result) and result[j]==ch:
                    count+=1
                    j+=1
                
                group.append(str(count))
                group.append(ch)
            new=""
            for value in group:
                new+=value
            reuslt=new
        return result"""
        