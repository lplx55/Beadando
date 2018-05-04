'''def convert2(lst,b1,b2):
    n=''
    L=[]
    for i in lst:
        i=str(i)
        n+=i
    n=int(n)
    if b1==10:
        while n>0:
            l=n%b2
            n//=b2
            L.append(l)
        return [i for i in L[::-1]]
    elif b1==2:
        sum=0
        lst=lst[::-1]
        for k in range(0,len(lst)):
            sum+=lst[k]*b1**k
        return sum
    else:
        return'''

def convert(lst,b1,b2):
    if b1!=10:
        B10=[]
        lst=lst[::-1]
        for i in range(len(lst)):
            a=lst[i]*(b1**i)
            B10.append(a)
        lst=list(str(sum(B10)))
    n = ''
    for i in lst:
        n += str(i)
    L=[]
    n=int(n)
    while n!=0:
        m=n%b2
        L.append(m)
        n=n//b2
    return L[::-1]


#main()
print(convert([1,2,4,1],5,7))