def count(s:str):
    vowel=['a','e','i','o','u']
    vowels=0
    consonants=0
    lowercase=""
    for ch in s:
        if 65<=ord(ch)<=90:
            lowercase+=chr(ord(ch)+32)
        else:
            lowercase+=ch
    for ch in lowercase:
        if 97<=ord(ch)<=122:
            if ch in vowel:
                vowels+=1
            else:
                consonants+=1
    return  vowels,consonants
def count(s:str):
    vowels=0
    consonants=0
    for ch in s:
        ascii=ord(ch)
        if 65<=ascii<=90:
            ascii+=32
        if 97<=ascii<=122:
            if chr(ascii) in "aeiou":
                vowels+=1
            else:
                consonants+=1
    return vowels,consonants
def count(s:str):
    vowels=0
    consonants=0
    for ch in s:
        ascii=ord(ch)
        if 65<=ascii<=90:
            ascii+=32
        if 97<=ascii<=122:
            if chr(ascii) in "aeiou":
                vowels+=1
    for ch in s:
            ascii=ord(ch)
            if 65<=ascii<=90:
                ascii+=32
            if 97<=ascii<=122:
                if chr(ascii) not in "aeiou":
                    consonants+=1
    return vowels,consonants


s="Hello World"
vowels,consonants=count(s)
print(vowels)
print(consonants)
        