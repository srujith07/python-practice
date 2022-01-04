def fibanocci(n1,n2):
    n=int(input("Enter n value: "))
    for i in range(n):
        c=n1+n2
        print(c,end=' ')
        n1=n2
        n2=c

fibanocci(0,1)