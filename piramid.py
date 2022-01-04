n = int(input())

for i in range(n):
    for a in range(i,n-1):
        print(".", end = " ")
    for b in range(i+1):
        print("0", end = " ")
    for b in range(i):
        print("0", end = " ") 
    for a in range(i,n-1):
        print(".", end = " ")    
    print()  
