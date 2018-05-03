def longestPalindrom(str):
#returns the longest palindromic substring of given string
    max=''
    #for i in range(0,len(str)):
        #for j in range(0,len(str),-1):
            #print(str[i])
            #if str[i]==str[j]:
                #if len(str[i:j])>len(max):
                    #max=str[i:j]
                    #print(str[i:]+str[:j])
    #return max
    l1=[]
    l2=[]
    for i in range((len(str)//2)+1):
        l1.append(str[i])
    for j in range(len(str)//2,len(str)):
        l2.append(str[j])
    if l1==l2[::-1]:
        return str
    elif l1==l1[::-1]:
        return l1
    elif l2==l2[::-1]:
        return l2
    return l1,l2

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
    return str[i:j+1]
    #for i in max:
        #if len(i)>maxl:
            #maxl=len(i)
        #return i

#main
print(longestPalindrom('arbaba'))
print(len('görög')//2)
#print(longestPalindrom2("görög"))