import string

def isPalindrom(str):
    if str[:]==str[::-1]:
        return True
    return False

def strip(s):
    unwanted=string.whitespace + string.punctuation
    for ch in s:
        if ch in unwanted:
            s=s.replace(ch, '')
    return s.lower()

def substrings(s):
    s=strip(s)
    sublist=[]
    palindromlist=[]
    for list in range(1,len(s)+1):
        for substr in range(0,list):
            lst='L'+str(list)
            lst=[]
            lst.append(s[substr:list])
            sublist.append(lst)
    for p in sublist:
        if isPalindrom(''.join(p)):
            palindromlist.append(p[0])
    return max(palindromlist, key=len)

#main
print(substrings('görög'))
#print(substrings('Madam I\'m Adam'))
#print(substrings('Alabama'))
