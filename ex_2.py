def convert(lst,b1,b2):
    for i in lst:
        if i>=b1 or i>=b2:
            return "Given numbers out of range."
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
