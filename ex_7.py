def longestPalindrom(str):
#gives back the longest palindromic substring of given string
    max=''
    for i in range(0,len(str)//2):
        for j in range(i, len(str)+1,-1):
            if str[i]==str[j]:
                if len(str[i:j])>len(max):
                    max=str[i:j]
    return max
#main
print(longestPalindrom("gag"))