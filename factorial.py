def factorail():
    n=int(input("Enter n value: "))
    f=1
    for i in range(1,n+1):
        f=f*i
    print("Factorial is ",f)
factorail()