def longestPalindrom(str):
#returns the longest palindromic substring of given string
    max=''
    for i in range(0,len(str)):
        for j in range(0,len(str),-1):
            if str[i]==str[j]:
                if len(str[i:j])>len(max):
                    max=str[i:j]
                print(str[i:]+str[:j])
    return max

def longestPalindrom2(str):
    i=0
    j=len(str)-1
    max=[]
    maxl=0
    while i<=len(str) and j>0:
        if str[i]==str[j]:
            max.append(str[i:j+1])
        i+=1
        j-=1
    for i in max:
        if len(i)>maxl:
            maxl=len(i)
        return i
#main
print(longestPalindrom2("arab"))