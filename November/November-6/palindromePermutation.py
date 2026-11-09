def palindrome_Permutation(s:str)->bool:
    """oddcharacters=set()
    visited=set()
    for i in range(len(s)):
        if s[i] not in visited:
            count=0
            for j in range(len(s)):
                if s[i]==s[j]:
                    count+=1
            visited.add(s[i])
            if count%2!=0:
                oddcharacters.add(s[i])
    if len(oddcharacters)>1:
        return False
    return True"""
    freq={}
    odd=False
    for ch in s:
        if ch not in freq:
            freq[ch]=1
        else:
            freq[ch]+=1
    for value in freq.values():
        if value%2!=0:
            if not odd:
                odd=True
            else:
                return False
    return True
print(palindrome_Permutation("code"))