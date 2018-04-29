def convert(lst,b1,b2):
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
        #lst=lst[::-1]
        for k in range(len(lst)-1,0,-1):
            m=lst[k]*(b2**k)
            L.append(m)
        return L

#main()
print(convert([1,1,0,0],2,10))