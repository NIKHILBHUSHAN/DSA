class Solution:
    def minOperations(self,s):
        '''
        n=len(s)
        pattern1=""
        pattern2=""
        for i in range(n):
            if i%2==0:
                pattern1+="0"
                pattern2+="1"
            else:
                pattern1+="1"
                pattern2+="0"
        count1=0
        count2=0
        for i in range(n):
            if s[i]!=pattern1[i]:
                count1+=1
            if s[i]!=pattern2[i]:
                count2+=1
        if count1<count2:
            return count1
        return count2
        '''
        count1=0
        count2=0
        for i in range(len(s)):
            if i%2==0:
                if s[i]!="0":
                    count1+=1
                if s[i]!="1":
                    count2+=1
            else:
                if s[i]!="1":
                    count1+=1
                if s[i]!="0":
                    count2+=1
        if count1<count2:
            return count1
        return count2