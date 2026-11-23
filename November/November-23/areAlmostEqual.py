class Solution:
    def areAlmostEqual(self,s1,s2):
        '''
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                arr=list(s1)
                arr[i],arr[j]=arr[j],arr[i]
                if arr==list(s2):
                    return True
        if s1==s2:
            return True
        return False
        '''
        if len(s1)!=len(s2):
            return False
        diff=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diff.append(i)
        if len(diff)==0:
            return True
        if len(diff)!=2:
            return False
        i=diff[0]
        j=diff[1]
        return s1[i]==s2[j] and s1[j]==s2[i]