n = int(input())

for i in range(1,n+1):
    for a in range(i,n-1):
        print(" ", end = " ")
    for b in range(1,i+1):
        print(b , end = " ")
    print()    
