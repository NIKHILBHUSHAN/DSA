class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result=[]

        if len(p)>len(s):
            return result

        p_count=[0]*26
        window_count=[0]*26

        for i in range(len(p)):
            p_count[ord(p[i])-ord('a')]+=1
            window_count[ord(s[i])-ord('a')]+=1

        if p_count==window_count:
            result.append(0)

        for i in range(len(p),len(s)):
            window_count[ord(s[i])-ord('a')]+=1
            window_count[ord(s[i-len(p)])-ord('a')]-=1

            if p_count==window_count:
                result.append(i-len(p)+1)

        return result


# Example
# s="cbaebabacd"
# p="abc"
# print(Solution().findAnagrams(s,p))
