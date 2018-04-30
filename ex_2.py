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
        sum=0
        lst=lst[::-1]
        for k in range(0,len(lst)):
            sum+=lst[k]*b1**k
        return sum
    else:
        return

#main()
print(convert([1,1,1,1],2,10))
