n = int(input())

for i in range(1,n+1):
    for a in range(i-1):
        print("^", end = " ")
    for j in range(i,n):
        print("*", end = " ")
    print()    
