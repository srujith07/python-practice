n = int(input())

for i in range(1,n+1):
    for a in range(i,n):
        print(" ",end ="")
    for j in range(1,i+1):
        print(j,end = " ")
        
    print()  
