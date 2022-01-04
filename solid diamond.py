n = int(input())

for i in range(n-1):
    for j in range(i,n):
        print(" ",end = " ")
    for b in range(i):
        print("*" ,end = " ")
    for c in range(i+1):
        print("*" ,end = " ")    
    print()
for i in range (n):
    for a in range(i+1):
        print(" " ,end = " ")
    for b in range(i,n-1):
        print("*" ,end = " ")
    for c in range(i,n):
        print("*" ,end = " ")     
    
    print()       
